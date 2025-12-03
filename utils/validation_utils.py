```python
# utils/validation_utils.py

import re

def validate_string(input_string, min_length=1, max_length=255):
    """
    Validate a string based on its length.

    Args:
        input_string (str): The string to be validated.
        min_length (int, optional): The minimum allowed length. Defaults to 1.
        max_length (int, optional): The maximum allowed length. Defaults to 255.

    Returns:
        bool: True if the string is valid, False otherwise.
    """
    return isinstance(input_string, str) and min_length <= len(input_string) <= max_length


def validate_email(email):
    """
    Validate an email address using a regular expression.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))


def validate_integer(input_value, min_value=None, max_value=None):
    """
    Validate an integer value.

    Args:
        input_value (int): The integer to be validated.
        min_value (int, optional): The minimum allowed value. Defaults to None.
        max_value (int, optional): The maximum allowed value. Defaults to None.

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
        region (str): The AWS region to be validated.

    Returns:
        bool: True if the region is valid, False otherwise.
    """
    # List of valid AWS regions (this list might not be exhaustive)
    valid_regions = [
        "us-east-1",
        "us-east-2",
        "us-west-1",
        "us-west-2",
        "ca-central-1",
        "ap-northeast-1",
        "ap-northeast-2",
        "ap-south-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "eu-central-1",
        "eu-west-1",
        "eu-west-2",
        "eu-west-3",
        "sa-east-1",
    ]
    return region in valid_regions
```
