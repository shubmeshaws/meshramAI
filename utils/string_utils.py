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
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def validate_ip(ip: str) -> bool:
    """
    Validate an IP address.

    Args:
    ip (str): The IP address to validate.

    Returns:
    bool: True if the IP is valid, False otherwise.
    """
    ip_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_regex, ip))

def slugify(s: str) -> str:
    """
    Convert a string to a slug.

    Args:
    s (str): The string to convert.

    Returns:
    str: The slugified string.
    """
    return re.sub(r"[^a-z0-9_\-]", "", s.lower().replace(" ", "-"))

def truncate(s: str, max_length: int) -> str:
    """
    Truncate a string to a maximum length.

    Args:
    s (str): The string to truncate.
    max_length (int): The maximum length.

    Returns:
    str: The truncated string.
    """
    if len(s) > max_length:
        return s[:max_length - 3] + "..."
    return s

def is_empty(s: str) -> bool:
    """
    Check if a string is empty.

    Args:
    s (str): The string to check.

    Returns:
    bool: True if the string is empty, False otherwise.
    """
    return not s.strip()
```
