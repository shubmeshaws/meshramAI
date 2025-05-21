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
  
  aws s3api delete-bucket \
    --bucket "$BUCKET_NAME" \
    --region "$REGION"

  echo "[SUCCESS] Bucket '$BUCKET_NAME' deleted from region '$REGION'."
}

