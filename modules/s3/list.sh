```bash
#!/bin/bash

function s3_list() {
  echo "[INFO] Listing S3 buckets..."
  if output=$(aws s3api list-buckets --query "Buckets[].Name" --output table 2>&1); then
    echo "$output"
    echo "[INFO] S3 buckets listed successfully."
  else
    echo "[ERROR] Failed to list S3 buckets. Error: $output"
  fi
}
```
