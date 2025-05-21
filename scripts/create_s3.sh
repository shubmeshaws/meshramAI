#!/bin/bash

set -e

BUCKET_NAME="$1"
REGION="$2"

if [[ -z "$BUCKET_NAME" || -z "$REGION" ]]; then
  echo "Usage: create_s3.sh <bucket-name> <region>"
  exit 1
fi

echo "Creating S3 bucket '$BUCKET_NAME' in region '$REGION'..."

aws s3api create-bucket \
  --bucket "$BUCKET_NAME" \
  --region "$REGION" \
  --create-bucket-configuration LocationConstraint="$REGION"

echo "✅ Bucket '$BUCKET_NAME' created successfully."

