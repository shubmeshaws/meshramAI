```python
"""
String utility functions.

This module provides functions for string manipulation and validation.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def validate_ip_address(ip: str) -> bool:
    """
    Validate an IP address.

    Args:
        ip (str): The IP address to validate.

    Returns:
        bool: True if the IP is valid, False otherwise.
    """
    ip_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return bool(re.match(ip_regex, ip))

def camel_case_to_snake_case(s: str) -> str:
    """
    Convert a camel case string to snake case.

    Args:
        s (str): The string to convert.

    Returns:
        str: The converted string.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

def snake_case_to_camel_case(s: str) -> str:
    """
    Convert a snake case string to camel case.

    Args:
        s (str): The string to convert.

    Returns:
        str: The converted string.
    """
    words = s.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

def remove_special_characters(s: str) -> str:
    """
    Remove special characters from a string.

    Args:
        s (str): The string to clean.

    Returns:
        str: The cleaned string.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', s)
```
