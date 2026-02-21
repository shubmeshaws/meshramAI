```python
"""
String utility functions.

This module provides functions for string manipulation and validation.
"""

import re

def is_valid_email(email: str) -> bool:
    """
    Checks if the provided email address is valid.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def is_valid_ip_address(ip_address: str) -> bool:
    """
    Checks if the provided IP address is valid.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_regex, ip_address))

def truncate_string(s: str, max_length: int) -> str:
    """
    Truncates a string to a specified maximum length.

    Args:
    s (str): The string to truncate.
    max_length (int): The maximum length of the string.

    Returns:
    str: The truncated string.
    """
    if len(s) > max_length:
        return s[:max_length] + "..."
    return s

def remove_special_chars(s: str) -> str:
    """
    Removes special characters from a string.

    Args:
    s (str): The string to remove special characters from.

    Returns:
    str: The string without special characters.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', s)
```
