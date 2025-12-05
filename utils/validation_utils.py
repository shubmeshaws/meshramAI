```python
"""
Validation utility functions.
"""

import re

def validate_string(input_string, min_length=1, max_length=255):
    """
    Validate a string based on length and content.

    Args:
        input_string (str): The string to validate.
        min_length (int, optional): Minimum length of the string. Defaults to 1.
        max_length (int, optional): Maximum length of the string. Defaults to 255.

    Returns:
        bool: True if the string is valid, False otherwise.
    """
    if not isinstance(input_string, str):
        return False
    if len(input_string) < min_length or len(input_string) > max_length:
        return False
    return True

def validate_integer(input_value, min_value=None, max_value=None):
    """
    Validate an integer based on value range.

    Args:
        input_value (int): The integer to validate.
        min_value (int, optional): Minimum value of the integer. Defaults to None.
        max_value (int, optional): Maximum value of the integer. Defaults to None.

    Returns:
        bool: True if the integer is valid, False otherwise.
    """
    if not isinstance(input_value, int):
        return False
    if min_value is not None and input_value < min_value:
        return False
    if max_value is not None and input_value > max_value:
        return False
    return True

def validate_aws_region(region):
    """
    Validate an AWS region.

    Args:
        region (str): The region to validate.

    Returns:
        bool: True if the region is valid, False otherwise.
    """
    # List of valid AWS regions
    valid_regions = ["us-east-1", "us-west-2", "eu-west-1", "ap-northeast-1"]
    return region in valid_regions

def validate_email(email):
    """
    Validate an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def validate_ip_address(ip_address):
    """
    Validate an IP address.

    Args:
        ip_address (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return bool(re.match(ip_address_regex, ip_address))
```
