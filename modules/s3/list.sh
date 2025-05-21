#!/bin/bash

function s3_list() {
  echo "[INFO] Listing S3 buckets..."
  aws s3api list-buckets --query "Buckets[].Name" --output table
}

