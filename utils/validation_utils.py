```python
import re
from typing import Any

def validate_string(input_string: str, min_length: int = 1, max_length: int = 255) -> bool:
    """
    Validate a string length.

    Args:
    input_string (str): The string to validate.
    min_length (int): The minimum allowed length. Defaults to 1.
    max_length (int): The maximum allowed length. Defaults to 255.

    Returns:
    bool: True if the string is valid, False otherwise.
    """
    return min_length <= len(input_string) <= max_length

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def validate_aws_region(region: str) -> bool:
    """
    Validate an AWS region.

    Args:
    region (str): The region to validate.

    Returns:
    bool: True if the region is valid, False otherwise.
    """
    valid_regions = ["us-east-1", "us-west-2", "eu-west-1", "ap-northeast-1"]
    return region in valid_regions

def validate_input_type(input_value: Any, expected_type: Any) -> bool:
    """
    Validate the type of an input.

    Args:
    input_value (Any): The value to validate.
    expected_type (Any): The expected type.

    Returns:
    bool: True if the input type is valid, False otherwise.
    """
    return isinstance(input_value, expected_type)

def validate_ip_address(ip_address: str) -> bool:
    """
    Validate an IP address.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_regex, ip_address))
```
