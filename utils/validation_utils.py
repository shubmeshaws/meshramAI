```python
# utils/validation_utils.py

import re
import ipaddress
from typing import Any

def validate_string(input_string: str, min_length: int = 1, max_length: int = 100) -> bool:
    """
    Validate if the input string meets the length requirements.

    Args:
    input_string (str): The input string to be validated.
    min_length (int): The minimum allowed length of the string (default is 1).
    max_length (int): The maximum allowed length of the string (default is 100).

    Returns:
    bool: True if the string is valid, False otherwise.
    """
    return min_length <= len(input_string) <= max_length

def validate_ip_address(ip_address: str) -> bool:
    """
    Validate if the input string is a valid IP address.

    Args:
    ip_address (str): The input string to be validated.

    Returns:
    bool: True if the string is a valid IP address, False otherwise.
    """
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False

def validate_email(email: str) -> bool:
    """
    Validate if the input string is a valid email address.

    Args:
    email (str): The input string to be validated.

    Returns:
    bool: True if the string is a valid email address, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def validate_type(input_value: Any, expected_type: type) -> bool:
    """
    Validate if the input value is of the expected type.

    Args:
    input_value (Any): The input value to be validated.
    expected_type (type): The expected type of the input value.

    Returns:
    bool: True if the input value is of the expected type, False otherwise.
    """
    return isinstance(input_value, expected_type)
```
