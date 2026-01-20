```python
import re
import boto3

def validate_aws_region(region):
    """
    Validate an AWS region.

    Args:
        region (str): The AWS region to validate.

    Returns:
        bool: True if the region is valid, False otherwise.
    """
    ec2 = boto3.client('ec2')
    try:
        ec2.describe_regions(RegionNames=[region])
        return True
    except Exception as e:
        return False


def validate_s3_bucket_name(bucket_name):
    """
    Validate an S3 bucket name.

    Args:
        bucket_name (str): The S3 bucket name to validate.

    Returns:
        bool: True if the bucket name is valid, False otherwise.
    """
    pattern = r'^[a-z0-9.-]{3,63}$'
    return bool(re.match(pattern, bucket_name))


def validate_ec2_instance_type(instance_type):
    """
    Validate an EC2 instance type.

    Args:
        instance_type (str): The EC2 instance type to validate.

    Returns:
        bool: True if the instance type is valid, False otherwise.
    """
    ec2 = boto3.client('ec2')
    try:
        ec2.describe_instance_types(InstanceTypes=[instance_type])
        return True
    except Exception as e:
        return False


def validate_vpc_id(vpc_id):
    """
    Validate a VPC ID.

    Args:
        vpc_id (str): The VPC ID to validate.

    Returns:
        bool: True if the VPC ID is valid, False otherwise.
    """
    ec2 = boto3.client('ec2')
    try:
        ec2.describe_vpcs(VpcIds=[vpc_id])
        return True
    except Exception as e:
        return False
```
