#!/bin/bash

function ec2_create() {
  NAME="$1"
  OS="$2"
  CPU="$3"
  MEM="$4"
  INPUT_REGION="$5"

  if [[ -z "$NAME" || -z "$OS" || -z "$CPU" || -z "$MEM" || -z "$INPUT_REGION" ]]; then
    echo "[ERROR] Usage: meshram ec2 create <name> <os> <cpu> <memory> <region>"
    return 1
  fi

  REGION="$(awk -F= -v region="$INPUT_REGION" '$1 == region { print $2 }' "$SCRIPT_DIR/regions.conf")"
  REGION="${REGION:-$INPUT_REGION}"

  echo "[INFO] Region set to $REGION"

  # Determine AMI ID
  case "$OS" in
    ubuntu24)
      AMI_ID=$(aws ec2 describe-images \
        --owners 099720109477 \
        --filters "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-jammy-24.04-amd64-server-*" \
                  "Name=state,Values=available" \
        --region "$REGION" \
        --query 'Images[*].[ImageId,CreationDate]' --output text | \
        sort -k2 -r | head -n1 | awk '{print $1}')
      ;;
    ubuntu22)
      AMI_ID=$(aws ec2 describe-images \
        --owners 099720109477 \
        --filters "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*" \
                  "Name=state,Values=available" \
        --region "$REGION" \
        --query 'Images[*].[ImageId,CreationDate]' --output text | \
        sort -k2 -r | head -n1 | awk '{print $1}')
      ;;
    amazonlinux2)
      AMI_ID=$(aws ec2 describe-images \
        --owners amazon \
        --filters "Name=name,Values=amzn2-ami-hvm-2.0.*-x86_64-gp2" \
                  "Name=state,Values=available" \
        --region "$REGION" \
        --query 'Images[*].[ImageId,CreationDate]' --output text | \
        sort -k2 -r | head -n1 | awk '{print $1}')
      ;;
    *)
      echo "[ERROR] Unsupported OS: $OS"
      return 1
      ;;
  esac

  echo "[INFO] AMI ID selected: $AMI_ID"

  # Determine instance type
  case "${CPU}-${MEM}" in
    1cpu-1gb) INSTANCE_TYPE="t2.micro" ;;
    2cpu-4gb) INSTANCE_TYPE="t2.medium" ;;
    2cpu-8gb) INSTANCE_TYPE="t3.large" ;;
    4cpu-16gb) INSTANCE_TYPE="t3.xlarge" ;;
    *) echo "[ERROR] Unsupported CPU/MEM combination"; return 1 ;;
  esac

  echo "[INFO] Instance type selected: $INSTANCE_TYPE"

  # Get default subnet ID
  SUBNET_ID=$(aws ec2 describe-subnets --region "$REGION" \
    --filters "Name=default-for-az,Values=true" \
    --query 'Subnets[0].SubnetId' --output text)

  # Get default security group
  SG_ID=$(aws ec2 describe-security-groups --region "$REGION" \
    --filters "Name=group-name,Values=default" \
    --query 'SecurityGroups[0].GroupId' --output text)

  # Create IAM Role for SSM
  ROLE_NAME="MeshramSSMRole"
  INSTANCE_PROFILE_NAME="MeshramSSMProfile"

  if ! aws iam get-instance-profile --instance-profile-name "$INSTANCE_PROFILE_NAME" >/dev/null 2>&1; then
    echo "[INFO] Creating IAM Role and Instance Profile for SSM"
    aws iam create-role --role-name "$ROLE_NAME" \
      --assume-role-policy-document file://"$SCRIPT_DIR/iam/ssm-trust.json"
    aws iam attach-role-policy --role-name "$ROLE_NAME" \
      --policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
    aws iam create-instance-profile --instance-profile-name "$INSTANCE_PROFILE_NAME"
    aws iam add-role-to-instance-profile --instance-profile-name "$INSTANCE_PROFILE_NAME" --role-name "$ROLE_NAME"
    sleep 10
  fi

  # Launch EC2 instance
  INSTANCE_ID=$(aws ec2 run-instances \
    --image-id "$AMI_ID" \
    --count 1 \
    --instance-type "$INSTANCE_TYPE" \
    --subnet-id "$SUBNET_ID" \
    --security-group-ids "$SG_ID" \
    --iam-instance-profile Name="$INSTANCE_PROFILE_NAME" \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$NAME}]" \
    --region "$REGION" \
    --query "Instances[0].InstanceId" --output text)

  echo "[SUCCESS] EC2 instance '$NAME' launched with ID: $INSTANCE_ID"
}

