```bash
#!/bin/bash

# ... (rest of the code remains the same)

function s3_create() {
  # ... (rest of the function remains the same)

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

  # Create the command to create the bucket
  create_bucket_cmd="aws s3api create-bucket --bucket $BUCKET_NAME --region $REGION --acl $ACL"
  if [ "$REGION" != "us-east-1" ]; then
    create_bucket_cmd+=" --create-bucket-configuration LocationConstraint=$REGION"
  fi

  # Try to execute the command
  if ! output=$($create_bucket_cmd 2>&1); then
    handle_error "Failed to create bucket '$BUCKET_NAME' in region '$REGION': $output" $ERROR_FAILED_TO_CREATE_BUCKET
    return
  fi

  echo "[SUCCESS] Bucket '$BUCKET_NAME' created in region '$REGION'."
}

# ACTUALLY CALL THE FUNCTION
s3_create "$@"
```
