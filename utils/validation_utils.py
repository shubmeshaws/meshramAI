```python
import re
from typing import Any

def validate_string(input_str: str, min_length: int = 1, max_length: int = 255) -> bool:
    """
    Validate a string input.

    Args:
    input_str (str): The input string to validate.
    min_length (int): The minimum allowed length of the string. Defaults to 1.
    max_length (int): The maximum allowed length of the string. Defaults to 255.

    Returns:
    bool: True if the string is valid, False otherwise.
    """
    return isinstance(input_str, str) and min_length <= len(input_str) <= max_length


def validate_integer(input_int: Any, min_value: int = 0, max_value: int = 100) -> bool:
    """
    Validate an integer input.

    Args:
    input_int (Any): The input integer to validate.
    min_value (int): The minimum allowed value of the integer. Defaults to 0.
    max_value (int): The maximum allowed value of the integer. Defaults to 100.

    Returns:
    bool: True if the integer is valid, False otherwise.
    """
    return isinstance(input_int, int) and min_value <= input_int <= max_value


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


def validate_aws_resource_id(resource_id: str) -> bool:
    """
    Validate an AWS resource ID.

    Args:
    resource_id (str): The AWS resource ID to validate.

    Returns:
    bool: True if the resource ID is valid, False otherwise.
    """
    # AWS resource IDs are typically in the format of "arn:aws:service:region:account-id:resource"
    arn_regex = r"^arn:aws:[a-z0-9-]+:[a-z0-9-]+:\d{12}:[a-zA-Z0-9-/_]+$"
    return bool(re.match(arn_regex, resource_id))
```
