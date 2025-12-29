```python
import os
import re
from typing import Dict

import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def validate_aws_credentials(aws_access_key_id: str, aws_secret_access_key: str) -> bool:
    """
    Validate AWS credentials by attempting to list S3 buckets.

    Args:
    aws_access_key_id (str): AWS access key ID.
    aws_secret_access_key (str): AWS secret access key.

    Returns:
    bool: True if credentials are valid, False otherwise.
    """
    try:
        s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        s3.list_buckets()
        return True
    except NoCredentialsError:
        return False
    except ClientError:
        return False

def validate_region_name(region_name: str) -> bool:
    """
    Validate an AWS region name.

    Args:
    region_name (str): AWS region name.

    Returns:
    bool: True if region name is valid, False otherwise.
    """
    valid_regions = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-southeast-1', 'ap-southeast-2', 'ap-south-1', 'sa-east-1']
    return region_name in valid_regions

def validate_file_path(file_path: str) -> bool:
    """
    Validate a file path by checking if the file exists.

    Args:
    file_path (str): File path.

    Returns:
    bool: True if file path is valid, False otherwise.
    """
    return os.path.isfile(file_path)

def validate_ec2_instance_id(instance_id: str) -> bool:
    """
    Validate an EC2 instance ID.

    Args:
    instance_id (str): EC2 instance ID.

    Returns:
    bool: True if instance ID is valid, False otherwise.
    """
    ec2 = boto3.client('ec2')
    try:
        ec2.describe_instances(InstanceIds=[instance_id])
        return True
    except ClientError:
        return False

def validate_s3_bucket_name(bucket_name: str) -> bool:
    """
    Validate an S3 bucket name.

    Args:
    bucket_name (str): S3 bucket name.

    Returns:
    bool: True if bucket name is valid, False otherwise.
    """
    s3 = boto3.client('s3')
    try:
        s3.head_bucket(Bucket=bucket_name)
        return True
    except ClientError:
        return False

def validate_vpc_id(vpc_id: str) -> bool:
    """
    Validate a VPC ID.

    Args:
    vpc_id (str): VPC ID.

    Returns:
    bool: True if VPC ID is valid, False otherwise.
    """
    ec2 = boto3.client('ec2')
    try:
        ec2.describe_vpcs(VpcIds=[vpc_id])
        return True
    except ClientError:
        return False

def validate_input_data(input_data: Dict) -> bool:
    """
    Validate input data by checking if all required fields are present and valid.

    Args:
    input_data (Dict): Input data.

    Returns:
    bool: True if input data is valid, False otherwise.
    """
    required_fields = ['aws_access_key_id', 'aws_secret_access_key', 'region_name']
    for field in required_fields:
        if field not in input_data:
            return False
    if not validate_aws_credentials(input_data['aws_access_key_id'], input_data['aws_secret_access_key']):
        return False
    if not validate_region_name(input_data['region_name']):
        return False
    return True
```
