```bash
#!/bin/bash

function get_available_images() {
  local OS="$1"
  local REGION="$2"

  case "$OS" in
    ubuntu24)
      FILTERS="Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-jammy-24.04-amd64-server-*"
      OWNER="099720109477"
      ;;
    ubuntu22)
      FILTERS="Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"
      OWNER="099720109477"
      ;;
    amazonlinux2)
      FILTERS="Name=name,Values=amzn2-ami-hvm-2.0.*-x86_64-gp2"
      OWNER="amazon"
      ;;
    *)
      echo "[ERROR] Unsupported OS: $OS"
      return 1
      ;;
  esac

  aws ec2 describe-images --owners "$OWNER" --filters "$FILTERS" "Name=state,Values=available" --region "$REGION" --query 'Images[*].[ImageId,CreationDate]' --output text 2>&1
  local RETURN_CODE=$?
  if [ $RETURN_CODE -ne 0 ]; then
    echo "[ERROR] Failed to describe images for $OS in $REGION: $(aws ec2 describe-images --owners "$OWNER" --filters "$FILTERS" "Name=state,Values=available" --region "$REGION" --query 'Images[*].[ImageId,CreationDate]' --output text 2>&1)"
    return 1
  fi
}

function get_latest_image_id() {
  local IMAGES="$1"

  if [ -z "$IMAGES" ]; then
    echo "[]"
    return
  fi

  echo "$IMAGES" | sort -k2 -r | head -n1 | awk '{print $1}'
}

function get_ami_id() {
  local OS="$1"
  local REGION="$2"

  AVAILABLE_IMAGES=$(get_available_images "$OS" "$REGION")
  if [ $? -ne 0 ]; then
    return 1
  fi

  LATEST_IMAGE_ID=$(get_latest_image_id "$AVAILABLE_IMAGES")
  if [ -z "$LATEST_IMAGE_ID" ]; then
    echo "[ERROR] Failed to get AMI ID for $OS"
    return 1
  fi

  echo "$LATEST_IMAGE_ID"
}
```
