```python
import re
import logging

from utils.aws_config import AWSConfig

logger = logging.getLogger(__name__)

def validate_aws_region(region):
    """
    Validate if the given region is a valid AWS region.

    Args:
    region (str): The region to validate.

    Returns:
    bool: True if the region is valid, False otherwise.
    """
    aws_config = AWSConfig()
    return region in aws_config.get_available_regions()

def validate_aws_account_id(account_id):
    """
    Validate if the given account ID is a valid AWS account ID.

    Args:
    account_id (str): The account ID to validate.

    Returns:
    bool: True if the account ID is valid, False otherwise.
    """
    pattern = re.compile(r'^\d{12}$')
    return bool(pattern.match(account_id))

def validate_bucket_name(bucket_name):
    """
    Validate if the given bucket name is a valid S3 bucket name.

    Args:
    bucket_name (str): The bucket name to validate.

    Returns:
    bool: True if the bucket name is valid, False otherwise.
    """
    pattern = re.compile(r'^[a-z0-9.-]{3,63}$')
    return bool(pattern.match(bucket_name))

def validate_vpc_id(vpc_id):
    """
    Validate if the given VPC ID is a valid VPC ID.

    Args:
    vpc_id (str): The VPC ID to validate.

    Returns:
    bool: True if the VPC ID is valid, False otherwise.
    """
    pattern = re.compile(r'^vpc-[a-f0-9]{8}$')
    return bool(pattern.match(vpc_id))

def validate_ec2_id(ec2_id):
    """
    Validate if the given EC2 ID is a valid EC2 ID.

    Args:
    ec2_id (str): The EC2 ID to validate.

    Returns:
    bool: True if the EC2 ID is valid, False otherwise.
    """
    pattern = re.compile(r'^i-[a-f0-9]{8}$')
    return bool(pattern.match(ec2_id))

def main():
    # Example usage:
    region = "us-west-2"
    account_id = "123456789012"
    bucket_name = "my-bucket"
    vpc_id = "vpc-12345678"
    ec2_id = "i-12345678"

    print(validate_aws_region(region))  # Output: True
    print(validate_aws_account_id(account_id))  # Output: True
    print(validate_bucket_name(bucket_name))  # Output: True
    print(validate_vpc_id(vpc_id))  # Output: True
    print(validate_ec2_id(ec2_id))  # Output: True

if __name__ == "__main__":
    main()
```
