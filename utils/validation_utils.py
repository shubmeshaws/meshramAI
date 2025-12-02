```python
"""
Validation utility functions.
"""

import re
import ipaddress

def validate_aws_region(region):
    """
    Validate an AWS region.

    Args:
        region (str): The region to validate.

    Returns:
        bool: True if the region is valid, False otherwise.
    """
    # List of valid AWS regions
    valid_regions = ["us-east-1", "us-west-2", "eu-west-1", "ap-southeast-1"]
    return region in valid_regions

def validate_ip_address(ip):
    """
    Validate an IP address.

    Args:
        ip (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def validate_cidr_block(cidr):
    """
    Validate a CIDR block.

    Args:
        cidr (str): The CIDR block to validate.

    Returns:
        bool: True if the CIDR block is valid, False otherwise.
    """
    try:
        ipaddress.ip_network(cidr, strict=False)
        return True
    except ValueError:
        return False

def validate_s3_bucket_name(bucket_name):
    """
    Validate an S3 bucket name.

    Args:
        bucket_name (str): The bucket name to validate.

    Returns:
        bool: True if the bucket name is valid, False otherwise.
    """
    # S3 bucket name must be between 3 and 63 characters long
    # and must be a valid DNS name
    if len(bucket_name) < 3 or len(bucket_name) > 63:
        return False
    if not re.match("^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$", bucket_name):
        return False
    return True

def validate_ec2_instance_id(instance_id):
    """
    Validate an EC2 instance ID.

    Args:
        instance_id (str): The instance ID to validate.

    Returns:
        bool: True if the instance ID is valid, False otherwise.
    """
    # EC2 instance ID must be in the format i-xxxxxxxxxxxxxxxxx
    if not re.match("^i-[a-f0-9]{8,17}$", instance_id):
        return False
    return True
```
