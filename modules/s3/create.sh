```bash
#!/bin/bash

SOURCE="${BASH_SOURCE[0]}"
while [ -L "$SOURCE" ]; do
  DIR="$(cd -P "$(dirname "$SOURCE")" >/dev/null 2>&1 && pwd)"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
done
SCRIPT_DIR="$(cd -P "$(dirname "$SOURCE")/../.." >/dev/null 2>&1 && pwd)"

function is_aws_cli_installed() {
  command -v aws &> /dev/null
}

function is_aws_cli_configured() {
  aws sts get-caller-identity &> /dev/null
}

function s3_create() {
  BUCKET_NAME="$1"
  INPUT_REGION="$2"
  ACL="${3:-private}"

  if [[ -z "$BUCKET_NAME" || -z "$INPUT_REGION" ]]; then
    echo "[ERROR] Usage: meshram s3 create <bucket-name> <region> [public|private]"
    return 1
  fi

  if [[ "$ACL" != "public" && "$ACL" != "private" ]]; then
    echo "[ERROR] Invalid ACL value. Only 'public' or 'private' are allowed."
    return 1
  fi

  if ! is_aws_cli_installed; then
    echo "[ERROR] AWS CLI is not installed or not in the system's PATH."
    return 1
  fi

  if ! is_aws_cli_configured; then
    echo "[ERROR] AWS CLI is not configured. Please run 'aws configure' to set up your credentials."
    return 1
  fi

  if [ ! -f "$SCRIPT_DIR/regions.conf" ]; then
    echo "[ERROR] File 'regions.conf' not found in '$SCRIPT_DIR'."
    return 1
  fi

  if ! REGION=$(awk -F= -v region="$INPUT_REGION" '$1 == region { print $2 }' "$SCRIPT_DIR/regions.conf" 2>/dev/null); then
    echo "[ERROR] Failed to read regions.conf or region '$INPUT_REGION' not found."
    return 1
  fi

  REGION="${REGION:-$INPUT_REGION}"

  echo "[INFO] Checking if bucket '$BUCKET_NAME' already exists..."
  if aws s3api head-bucket --bucket "$BUCKET_NAME" &> /dev/null; then
    echo "[INFO] Bucket '$BUCKET_NAME' already exists."
    return 0
  fi

  echo "[INFO] Creating bucket '$BUCKET_NAME' in region '$REGION' with ACL '$ACL'..."

  if [[ "$REGION" == "us-east-1" ]]; then
    output=$(aws s3api create-bucket --bucket "$BUCKET_NAME" --region "$REGION" --acl "$ACL" 2>&1)
    status=$?
  else
    output=$(aws s3api create-bucket --bucket "$BUCKET_NAME" --region "$REGION" --create-bucket-configuration LocationConstraint="$REGION" --acl "$ACL" 2>&1)
    status=$?
  fi

  if [ $status -ne 0 ]; then
    case $output in
      *"BucketAlreadyOwnedByYou"*)
        echo "[ERROR] Bucket '$BUCKET_NAME' already exists and is owned by you in region '$REGION'."
        ;;
      *"BucketAlreadyExists"*)
        echo "[ERROR] Bucket '$BUCKET_NAME' already exists and is owned by another account."
        ;;
      *"InvalidAccessKeyId"*)
        echo "[ERROR] Invalid access key ID. Please check your AWS credentials."
        ;;
      *"SignatureDoesNotMatch"*)
        echo "[ERROR] Signature does not match. Please check your AWS credentials."
        ;;
      *)
        echo "[ERROR] Failed to create bucket '$BUCKET_NAME' in region '$REGION':"
        echo "$output"
        ;;
    esac
    return 1
  fi

  echo "[SUCCESS] Bucket '$BUCKET_NAME' created in region '$REGION'."
}

# ACTUALLY CALL THE FUNCTION
s3_create "$@"
```
