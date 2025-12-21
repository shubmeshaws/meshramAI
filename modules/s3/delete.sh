```bash
#!/bin/bash

set -eu

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
  if ! timeout 10s aws s3 ls "s3://$INPUT_REGION" &> /dev/null; then
    echo "[ERROR] Invalid region '$INPUT_REGION'. Please check the region name."
    return 1
  fi
}

function validate_aws_cli() {
  if ! command -v aws &> /dev/null; then
    echo "[ERROR] AWS CLI is not installed or not in the system's PATH."
    return 1
  fi
  if ! timeout 10s aws sts get-caller-identity &> /dev/null; then
    echo "[ERROR] AWS CLI is not configured properly. Please run 'aws configure' to set up your AWS credentials."
    return 1
  fi
}

function s3_delete() {
  BUCKET_NAME="$1"
  INPUT_REGION="$2"

  validate_bucket_name "$BUCKET_NAME"
  validate_region "$INPUT_REGION"
  validate_aws_cli

  REGION="$(awk -F= -v region="$INPUT_REGION" '$1 == region { print $2 }' "$SCRIPT_DIR/regions.conf")"
  REGION="${REGION:-$INPUT_REGION}"

  if ! output=$(timeout 30s aws s3api head-bucket --bucket "$BUCKET_NAME" --region "$REGION" 2>&1); then
    if echo "$output" | grep -q "Not Found"; then
      echo "[WARNING] Bucket '$BUCKET_NAME' does not exist in region '$REGION'."
      return 0
    elif echo "$output" | grep -q "Timeout"; then
      echo "[ERROR] Failed to check bucket '$BUCKET_NAME' in region '$REGION': timed out"
      return 1
    else
      echo "[ERROR] Failed to check bucket '$BUCKET_NAME' in region '$REGION': $output"
      return 1
    fi
  fi

  echo "[WARNING] Deleting S3 bucket '$BUCKET_NAME' in region '$REGION' will PERMANENTLY DELETE all its contents. Are you sure? (y/n)"
  read -r confirmation
  if [[ "$confirmation" != "y" ]]; then
    echo "[INFO] Deletion cancelled."
    return 0
  fi

  echo "[INFO] Emptying bucket '$BUCKET_NAME'..."
  if ! output=$(timeout 300s aws s3 rm s3://"$BUCKET_NAME" --recursive --region "$REGION" 2>&1); then
    if echo "$output" | grep -q "Timeout"; then
      echo "[ERROR] Failed to empty bucket '$BUCKET_NAME' in region '$REGION': timed out"
    else
      echo "[ERROR] Failed to empty bucket '$BUCKET_NAME' in region '$REGION': $output"
    fi
    return 1
  fi

  # Delete the bucket
  if ! output=$(timeout 30s aws s3api delete-bucket --bucket "$BUCKET_NAME" --region "$REGION" 2>&1); then
    if echo "$output" | grep -q "The bucket is not empty"; then
      echo "[ERROR] Failed to delete bucket '$BUCKET_NAME' in region '$REGION': Bucket is not empty"
    elif echo "$output" | grep -q "Timeout"; then
      echo "[ERROR] Failed to delete bucket '$BUCKET_NAME' in region '$REGION': timed out"
    else
      echo "[ERROR] Failed to delete bucket '$BUCKET_NAME' in region '$REGION': $output"
    fi
    return 1
  fi

  echo "[SUCCESS] Bucket '$BUCKET_NAME' deleted from region '$REGION'."
}
```
