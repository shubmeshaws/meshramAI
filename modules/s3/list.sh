```bash
#!/bin/bash

function s3_list() {
  # Check if AWS CLI is installed
  if ! command -v aws &> /dev/null; then
    echo "[ERROR] AWS CLI is not installed. Please install and configure it before proceeding."
    return
  fi

  # Check if AWS CLI is configured
  if [ -z "${AWS_ACCESS_KEY_ID}" ] || [ -z "${AWS_SECRET_ACCESS_KEY}" ]; then
    echo "[ERROR] AWS CLI is not configured. Please set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables."
    return
  fi

  echo "[INFO] Listing S3 buckets..."
  if output=$(aws s3api list-buckets --query "Buckets[].Name" --output table 2>&1); then
    echo "$output"
    echo "[INFO] S3 buckets listed successfully."
  else
    echo "[ERROR] Failed to list S3 buckets. Error: $output"
  fi
}
```
