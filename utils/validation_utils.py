```python
import re
import boto3
from typing import Any

def validate_string(input_str: str, min_length: int = 1, max_length: int = 255) -> bool:
    """
    Validate a string based on its length.

    Args:
    input_str (str): The input string to validate.
    min_length (int): The minimum allowed length (default: 1).
    max_length (int): The maximum allowed length (default: 255).

    Returns:
    bool: True if the string is valid, False otherwise.
    """
    return min_length <= len(input_str) <= max_length


def validate_integer(input_int: Any, min_value: int = 0, max_value: int = 1000) -> bool:
    """
    Validate an integer based on its value.

    Args:
    input_int (Any): The input integer to validate.
    min_value (int): The minimum allowed value (default: 0).
    max_value (int): The maximum allowed value (default: 1000).

    Returns:
    bool: True if the integer is valid, False otherwise.
    """
    if not isinstance(input_int, int):
        return False
    return min_value <= input_int <= max_value


def validate_aws_region(region: str) -> bool:
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
    except Exception:
        return False


def validate_aws_account_id(account_id: str) -> bool:
    """
    Validate an AWS account ID.

    Args:
    account_id (str): The AWS account ID to validate.

    Returns:
    bool: True if the account ID is valid, False otherwise.
    """
    pattern = re.compile(r'^\d{12}$')
    return bool(pattern.match(account_id))


def validate_iam_role(role_name: str) -> bool:
    """
    Validate an IAM role.

    Args:
    role_name (str): The IAM role to validate.

    Returns:
    bool: True if the role is valid, False otherwise.
    """
    iam = boto3.client('iam')
    try:
        iam.get_role(RoleName=role_name)
        return True
    except Exception:
        return False
```
