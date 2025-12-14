```python
"""
String Validation Utility
==========================

This module provides functions for validating and sanitizing string inputs.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
    - email (str): The email address to validate.

    Returns:
    - bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def validate_ip_address(ip_address: str) -> bool:
    """
    Validate an IP address.

    Args:
    - ip_address (str): The IP address to validate.

    Returns:
    - bool: True if the IP address is valid, False otherwise.
    """
    ip_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_regex, ip_address))

def sanitize_string(input_string: str) -> str:
    """
    Sanitize a string by removing leading/trailing whitespace and non-alphanumeric characters.

    Args:
    - input_string (str): The string to sanitize.

    Returns:
    - str: The sanitized string.
    """
    return re.sub(r"[^a-zA-Z0-9_]", "", input_string.strip())

def validate_string_length(input_string: str, min_length: int = 1, max_length: int = 255) -> bool:
    """
    Validate the length of a string.

    Args:
    - input_string (str): The string to validate.
    - min_length (int): The minimum allowed length (default: 1).
    - max_length (int): The maximum allowed length (default: 255).

    Returns:
    - bool: True if the string length is valid, False otherwise.
    """
    return min_length <= len(input_string) <= max_length
```
