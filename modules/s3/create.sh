```bash
#!/bin/bash

SOURCE="${BASH_SOURCE[0]}"
while [ -L "$SOURCE" ]; do
  DIR="$(cd -P "$(dirname "$SOURCE")" >/dev/null 2>&1 && pwd)"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
done
SCRIPT_DIR="$(cd -P "$(dirname "$SOURCE")/../.." >/dev/null 2>&1 && pwd)"

# Define specific error codes
ERROR_AWS_CLI_NOT_INSTALLED=10
ERROR_AWS_CLI_NOT_CONFIGURED=11
ERROR_INVALID_BUCKET_NAME=20
ERROR_INVALID_REGION_NAME=30
ERROR_REGION_NOT_FOUND=40
ERROR_BUCKET_ALREADY_EXISTS=50
ERROR_FAILED_TO_CREATE_BUCKET=60
ERROR_INVALID_REGIONS_CONF=70

function is_aws_cli_installed() {
  command -v aws &> /dev/null
}

function is_aws_cli_configured() {
  aws sts get-caller-identity &> /dev/null
}

function is_valid_bucket_name() {
  local BUCKET_NAME="$1"
  # Check if the bucket name is not empty and its length is between 3 and 63 characters
  if [ ${#BUCKET_NAME} -lt 3 ] || [ ${#BUCKET_NAME} -gt 63 ]; then
    return 1
  fi
  # Check if the bucket name only contains lowercase letters, numbers, and hyphens
  if ! [[ "$BUCKET_NAME" =~ ^[a-z0-9-]+$ ]]; then
    return 1
  fi
  # Check if the bucket name does not start or end with a hyphen
  if [[ "$BUCKET_NAME" =~ ^- ]] || [[ "$BUCKET_NAME" =~ -$ ]]; then
    return 1
  fi
  return 0
}

function is_valid_region_name() {
  local REGION_NAME="$1"
  # Check if the region name only contains letters, numbers, and hyphens
  if ! [[ "$REGION_NAME" =~ ^[a-zA-Z0-9-]+$ ]]; then
    return 1
  fi
  # Check if the region name is not empty
  if [ -z "$REGION_NAME" ]; then
    return 1
  fi
  return 0
}

function handle_error() {
  local ERROR_MESSAGE="$1"
  local ERROR_CODE="$2"
  echo "[ERROR] $ERROR_MESSAGE" >&2
  return "$ERROR_CODE"
}

function validate_regions_conf() {
  local FILE_PATH="$1"
  local REGION_NAMES=()

  if [ ! -f "$FILE_PATH" ]; then
    handle_error "File '$FILE_PATH' not found." $ERROR_INVALID_REGIONS_CONF
    return
  fi

  if [ ! -s "$FILE_PATH" ]; then
    handle_error "File '$FILE_PATH' is empty." $ERROR_INVALID_REGIONS_CONF
    return
  fi

  while IFS= read -r line; do
    line=$(echo "$line" | tr -d '[:space:]')
    if [ -z "$line" ]; then
      continue
    fi

    if ! [[ "$line" =~ ^[a-zA-Z0-9-]+=[a-zA-Z0-9-]+$ ]]; then
      handle_error "Invalid format in '$FILE_PATH': '$line'" $ERROR_INVALID_REGIONS_CONF
      return
    fi

    region_name=$(echo "$line" | cut -d '=' -f 1)
    if [[ " ${REGION_NAMES[@]} " =~ " $region_name " ]]; then
      handle_error "Duplicate region name '$region_name' in '$FILE_PATH'" $ERROR_INVALID_REGIONS_CONF
      return
    fi

    REGION_NAMES+=("$region_name")
  done < "$FILE_PATH"
}

function s3_create() {
  BUCKET_NAME="$1"
  INPUT_REGION="$2"
  ACL="${3:-private}"

  if [[ -z "$BUCKET_NAME" || -z "$INPUT_REGION" ]]; then
    handle_error "Usage: meshram s3 create <bucket-name> <region> [public|private]" 1
    return
  fi

  if [[ "$ACL" != "public" && "$ACL" != "private" ]]; then
    handle_error "Invalid ACL value. Only 'public' or 'private' are allowed." 1
    return
  fi

  if ! is_aws_cli_installed; then
    handle_error "AWS CLI is not installed or not in the system's PATH." $ERROR_AWS_CLI_NOT_INSTALLED
    return
  fi

  if ! is_aws_cli_configured; then
    handle_error "AWS CLI is not configured. Please run 'aws configure' to set up your credentials." $ERROR_AWS_CLI_NOT_CONFIGURED
    return
  fi

  validate_regions_conf "$SCRIPT_DIR/regions.conf"

  if ! is_valid_bucket_name "$BUCKET_NAME"; then
    handle_error "Invalid bucket name '$BUCKET_NAME'. Please use a valid bucket name (only lowercase letters, numbers, and hyphens, between 3 and 63 characters, and does not start or end with a hyphen)." $ERROR_INVALID_BUCKET_NAME
    return
  fi

  if ! is_valid_region_name "$INPUT_REGION"; then
    handle_error "Invalid region name '$INPUT_REGION'. Please use a valid region name (only letters, numbers, and hyphens, not empty)." $ERROR_INVALID_REGION_NAME
    return
  fi

  REGION=$(awk -F= -v region="$INPUT_REGION" '$1 == region { print $2 }' "$SCRIPT_DIR/regions.conf" 2>/dev/null)
  if [ -z "$REGION" ]; then
    handle_error "Region '$INPUT_REGION' not found in 'regions.conf'." $ERROR_REGION_NOT_FOUND
    return
  fi

  REGION="${REGION:-$INPUT_REGION}"

  # Check if the region is valid
  if ! grep -q "^$INPUT_REGION=" "$SCRIPT_DIR/regions.conf"; then
    handle_error "Region '$INPUT_REGION' does not match the format in 'regions.conf'." $ERROR_REGION_NOT_FOUND
    return
  fi

  echo "[INFO] Checking if bucket '$BUCKET_NAME' already exists..."
  if ! output=$(aws s3api head-bucket --bucket "$BUCKET_NAME" 2>&1); then
    if echo "$output" | grep -q "404"; then
      echo "[INFO] Bucket '$BUCKET_NAME' does not exist."
    else
      handle_error "Failed to check if bucket '$BUCKET_NAME' exists: $output" 1
      return
    fi
  else
    echo "[INFO] Bucket '$BUCKET_NAME' already exists."
    handle_error "Bucket '$BUCKET_NAME' already exists." $ERROR_BUCKET_ALREADY_EXISTS
    return
  fi

  echo "[INFO] Creating bucket '$BUCKET_NAME' in region '$REGION' with ACL '$ACL'..."

  if [[ "$REGION" == "us-east-1" ]]; then
    if ! output=$(aws s3api create-bucket --bucket "$BUCKET_NAME" --region "$REGION" --acl "$ACL" 2>&1); then
      handle_error "Failed to create bucket '$BUCKET_NAME' in region '$REGION': $output" $ERROR_FAILED_TO_CREATE_BUCKET
      return
    fi
  else
    if ! output=$(aws s3api create-bucket --bucket "$BUCKET_NAME" --region "$REGION" --create-bucket-configuration LocationConstraint="$REGION" --acl "$ACL" 2>&1); then
      handle_error "Failed to create bucket '$BUCKET_NAME' in region '$REGION': $output" $ERROR_FAILED_TO_CREATE_BUCKET
      return
    fi
  fi

  echo "[SUCCESS] Bucket '$BUCKET_NAME' created in region '$REGION'."
}

# ACTUALLY CALL THE FUNCTION
s3_create "$@"
```
