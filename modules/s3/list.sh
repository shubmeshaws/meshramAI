```bash
#!/bin/bash

function handle_error() {
  local exit_code=$1
  local error_output=$2
  case $exit_code in
    124)
      echo "[ERROR] AWS CLI command timed out after 30 seconds. Check your network connection or AWS service status. Error: $error_output"
      ;;
    130)
      echo "[ERROR] AWS CLI command was interrupted. Please try again. Error: $error_output"
      ;;
    255)
      echo "[ERROR] AWS CLI command failed with an unknown error. Check the AWS CLI version and configuration. Error: $error_output"
      ;;
    *)
      if echo "$error_output" | grep -q "AccessDenied"; then
        echo "[ERROR] Access denied to list S3 buckets. Please ensure the AWS IAM role or user has the necessary permissions (s3:ListBuckets). Error: $error_output"
      else
        echo "[ERROR] Failed to list S3 buckets with exit code $exit_code. Error: $error_output"
      fi
      ;;
  esac
}

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
  if output=$(timeout 30s aws s3api list-buckets --query "Buckets[].Name" --output table 2>&1); then
    echo "$output"
    echo "[INFO] S3 buckets listed successfully."
  else
    handle_error $? "$output"
  fi
}

s3_list
```
