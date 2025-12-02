```python
import re
import ipaddress
import boto3
from botocore.exceptions import ClientError

def validate_aws_credentials(access_key, secret_key):
    """
    Validate AWS credentials by attempting to list S3 buckets.

    Args:
        access_key (str): AWS access key.
        secret_key (str): AWS secret key.

    Returns:
        bool: True if credentials are valid, False otherwise.
    """
    try:
        s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        s3.list_buckets()
        return True
    except ClientError:
        return False

def validate_ip_address(ip):
    """
    Validate an IP address.

    Args:
        ip (str): IP address to validate.

    Returns:
        bool: True if IP address is valid, False otherwise.
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
        cidr (str): CIDR block to validate.

    Returns:
        bool: True if CIDR block is valid, False otherwise.
    """
    try:
        ipaddress.ip_network(cidr, strict=False)
        return True
    except ValueError:
        return False

def validate_region(region):
    """
    Validate an AWS region.

    Args:
        region (str): AWS region to validate.

    Returns:
        bool: True if region is valid, False otherwise.
    """
    valid_regions = ['us-east-1', 'us-west-1', 'us-west-2', 'eu-west-1', 'eu-central-1', 'ap-northeast-1', 'ap-southeast-1', 'ap-southeast-2']
    return region in valid_regions

def validate_access_key(access_key):
    """
    Validate an AWS access key.

    Args:
        access_key (str): AWS access key to validate.

    Returns:
        bool: True if access key is valid, False otherwise.
    """
    pattern = r'^AKIA[0-9A-Z]{16}$'
    return bool(re.match(pattern, access_key))

def validate_secret_key(secret_key):
    """
    Validate an AWS secret key.

    Args:
        secret_key (str): AWS secret key to validate.

    Returns:
        bool: True if secret key is valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9/+=]{40}$'
    return bool(re.match(pattern, secret_key))
```
