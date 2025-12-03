```bash
#!/bin/bash

function s3_delete() {
  BUCKET_NAME="$1"
  INPUT_REGION="$2"

  if [[ -z "$BUCKET_NAME" || -z "$INPUT_REGION" ]]; then
    echo "[ERROR] Usage: meshram s3 delete <bucket-name> <region>"
    return 1
  fi

  # Validate bucket name using regex pattern
  if ! [[ "$BUCKET_NAME" =~ ^[a-z0-9.-]{3,63}$ ]]; then
    echo "[ERROR] Invalid bucket name '$BUCKET_NAME'. Bucket names must be between 3 and 63 characters long and can only contain lowercase letters, numbers, periods, and hyphens."
    return 1
  fi

  REGION="$(awk -F= -v region="$INPUT_REGION" '$1 == region { print $2 }' "$SCRIPT_DIR/regions.conf")"
  REGION="${REGION:-$INPUT_REGION}"

  if ! aws s3api head-bucket --bucket "$BUCKET_NAME" --region "$REGION" &> /dev/null; then
    case $? in
      254) # No such bucket
        echo "[WARNING] Bucket '$BUCKET_NAME' does not exist in region '$REGION'."
        return 0
        ;;
      255) # AWS CLI error
        echo "[ERROR] AWS CLI error: Failed to check bucket '$BUCKET_NAME' in region '$REGION'"
        return 1
        ;;
      *) # Other errors
        echo "[ERROR] Unknown error: Failed to check bucket '$BUCKET_NAME' in region '$REGION'"
        return 1
        ;;
    esac
  fi

  echo "[WARNING] Deleting S3 bucket '$BUCKET_NAME' in region '$REGION'..."
  
  if ! output=$(aws s3api delete-bucket --bucket "$BUCKET_NAME" --region "$REGION" 2>&1); then
    case $? in
      254) # Bucket is not empty
        echo "[ERROR] Failed to delete bucket '$BUCKET_NAME' in region '$REGION': Bucket is not empty"
        return 1
        ;;
      255) # AWS CLI error
        echo "[ERROR] AWS CLI error: Failed to delete bucket '$BUCKET_NAME' in region '$REGION': $output"
        return 1
        ;;
      *) # Other errors
        echo "[ERROR] Unknown error: Failed to delete bucket '$BUCKET_NAME' in region '$REGION': $output"
        return 1
        ;;
    esac
  fi

  echo "[SUCCESS] Bucket '$BUCKET_NAME' deleted from region '$REGION'."
}
```
