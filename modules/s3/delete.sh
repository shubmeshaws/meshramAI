```bash
#!/bin/bash

function s3_delete() {
  BUCKET_NAME="$1"
  INPUT_REGION="$2"

  if [[ -z "$BUCKET_NAME" || -z "$INPUT_REGION" ]]; then
    echo "[ERROR] Usage: meshram s3 delete <bucket-name> <region>"
    return 1
  fi

  REGION="$(awk -F= -v region="$INPUT_REGION" '$1 == region { print $2 }' "$SCRIPT_DIR/regions.conf")"
  REGION="${REGION:-$INPUT_REGION}"

  echo "[WARNING] Deleting S3 bucket '$BUCKET_NAME' in region '$REGION'..."
  
  if ! aws s3api delete-bucket --bucket "$BUCKET_NAME" --region "$REGION"; then
    echo "[ERROR] Failed to delete bucket '$BUCKET_NAME' in region '$REGION': $?"
    return 1
  fi

  echo "[SUCCESS] Bucket '$BUCKET_NAME' deleted from region '$REGION'."
}
```
