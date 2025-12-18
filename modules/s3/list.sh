```bash
#!/bin/bash

function s3_list() {
  # Check if AWS CLI is installed
  if ! command -v aws &> /dev/null; then
    echo "[ERROR] AWS CLI is not installed. Please install and configure it before proceeding."
    return
  fi

  # Validate AWS CLI configuration by checking access to STS
  if ! aws sts get-caller-identity &> /dev/null; then
    echo "[ERROR] Invalid AWS CLI configuration. Please verify your AWS credentials."
    return
  fi

  echo "[INFO] Listing S3 buckets..."
  if output=$(aws s3api list-buckets --query "Buckets[].Name" --output table 2>&1); then
    echo "$output"
    echo "[INFO] S3 buckets listed successfully."
  else
    case $? in
      255)
        echo "[ERROR] AWS CLI command failed with an unknown error."
        ;;
      *)
        echo "[ERROR] Failed to list S3 buckets. Error: $output"
        ;;
    esac
  fi
}
```
