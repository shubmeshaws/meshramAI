```bash
#!/bin/bash

set -eu

# Set default timeouts if not provided
DEFAULT_AWS_TIMEOUT=30
DEFAULT_S3_RM_TIMEOUT=300
DEFAULT_AWS_STS_TIMEOUT=10

# Allow configuration through environment variables
AWS_TIMEOUT=${AWS_TIMEOUT:-$DEFAULT_AWS_TIMEOUT}
S3_RM_TIMEOUT=${S3_RM_TIMEOUT:-$DEFAULT_S3_RM_TIMEOUT}
AWS_STS_TIMEOUT=${AWS_STS_TIMEOUT:-$DEFAULT_AWS_STS_TIMEOUT}

function validate_bucket_name() {
  local BUCKET_NAME="$1"
  if [[ -z "$BUCKET_NAME" ]]; then
    echo "[ERROR] Bucket name is required"
    return 1
  fi
  if ! [[ "$BUCKET_NAME" =~ ^[a-z0-9.-]{3,63}$ ]]; then
    echo "[ERROR] Invalid bucket name '$BUCKET_NAME'. Bucket names must be between 3 and 63 characters long and can only contain lowercase letters, numbers, periods, and hyphens."
    return 1
  fi
}

function validate_region() {
  local INPUT_REGION="$1"
  if [[ -z "$INPUT_REGION" ]]; then
    echo "[ERROR] Region is required"
    return 1
  fi
  if ! timeout "$AWS_STS_TIMEOUT"s aws s3 ls "s3://$INPUT_REGION" &> /dev/null; then
    echo "[ERROR] Invalid region '$INPUT_REGION'. Please check the region name."
    return 1
  fi
}

function validate_aws_cli() {
  if ! command -v aws &> /dev/null; then
    echo "[ERROR] AWS CLI is not installed or not in the system's PATH."
    return 1
  fi
  if ! timeout "$AWS_STS_TIMEOUT"s aws sts get-caller-identity &> /dev/null; then
    echo "[ERROR] AWS CLI is not configured properly. Please run 'aws configure' to set up your AWS credentials."
    return 1
  fi
}

function handle_aws_error() {
  local output="$1"
  local command="$2"
  if echo "$output" | grep -q "Not Found"; then
    echo "[WARNING] $command failed: Not Found"
  elif echo "$output" | grep -q "Timeout"; then
    echo "[ERROR] $command failed: timed out"
  elif echo "$output" | grep -q "The bucket is not empty"; then
    echo "[ERROR] $command failed: Bucket is not empty"
  else
    echo "[ERROR] $command failed: $output"
  fi
  return 1
}

function get_confirmation() {
  local prompt="$1"
  while true; do
    echo "$prompt"
    read -r confirmation
    case "$confirmation" in
      y) return 0 ;;
      n) return 1 ;;
      *) echo "[ERROR] Invalid input. Please enter 'y' or 'n'." ;;
    esac
  done
}

function retry_aws_command() {
  local command="$1"
  local timeout="$2"
  local max_retries="${3:-3}"
  local retry_count=0
  while [ $retry_count -lt $max_retries ]; do
    if ! output=$(timeout "$timeout"s $command 2>&1); then
      handle_aws_error "$output" "$command"
      ((retry_count++))
      sleep 1
    else
      echo "$output"
      return 0
    fi
  done
  echo "[ERROR] Command '$command' failed after $max_retries retries"
  return 1
}

SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
if [ ! -f "$SCRIPT_DIR/regions.conf" ]; then
  echo "[ERROR] regions.conf file not found in $SCRIPT_DIR"
  exit 1
fi

if [ ! -s "$SCRIPT_DIR/regions.conf" ]; then
  echo "[ERROR] regions.conf file is empty in $SCRIPT_DIR"
  exit 1
fi

# Validate regions.conf file format
if ! awk -F= '{if (NF != 2) {print "[ERROR] Invalid regions.conf format. Each line must be in the format 'region=endpoint'"; exit 1}}' "$SCRIPT_DIR/regions.conf" &> /dev/null; then
  exit 1
fi

# Check for duplicate region entries in regions.conf
if awk -F= '!seen[$1]++ {print $1}' "$SCRIPT_DIR/regions.conf" | sort -u | wc -l -ne $(awk -F= '{print $1}' "$SCRIPT_DIR/regions.conf" | sort -u | wc -l); then
  echo "[ERROR] regions.conf file contains duplicate region entries"
  exit 1
fi

function s3_delete() {
  BUCKET_NAME="$1"
  INPUT_REGION="$2"

  validate_bucket_name "$BUCKET_NAME"
  validate_region "$INPUT_REGION"
  validate_aws_cli

  REGION="$(awk -F= -v region="$INPUT_REGION" '$1 == region { print $2 }' "$SCRIPT_DIR/regions.conf")"
  REGION="${REGION:-$INPUT_REGION}"

  if ! output=$(retry_aws_command "aws s3api head-bucket --bucket $BUCKET_NAME --region $REGION" "$AWS_TIMEOUT"); then
    return $?
  fi

  if ! get_confirmation "[WARNING] Deleting S3 bucket '$BUCKET_NAME' in region '$REGION' will PERMANENTLY DELETE all its contents. Are you sure? (y/n)"; then
    echo "[INFO] Deletion cancelled."
    return 0
  fi

  echo "[INFO] Emptying bucket '$BUCKET_NAME'..."
  if ! output=$(retry_aws_command "aws s3 rm s3://$BUCKET_NAME --recursive --region $REGION" "$S3_RM_TIMEOUT"); then
    return $?
  fi

  if ! get_confirmation "[WARNING] Bucket '$BUCKET_NAME' has been emptied. Are you sure you want to delete it? (y/n)"; then
    echo "[INFO] Deletion cancelled."
    return 0
  fi

  # Delete the bucket
  if ! output=$(retry_aws_command "aws s3api delete-bucket --bucket $BUCKET_NAME --region $REGION" "$AWS_TIMEOUT"); then
    return $?
  fi

  echo "[SUCCESS] Bucket '$BUCKET_NAME' deleted from region '$REGION'."
}
```
