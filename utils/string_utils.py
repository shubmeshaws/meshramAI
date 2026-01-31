```python
"""
String utility functions for string manipulation and validation.
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

def strip_whitespace(s: str) -> str:
    """
    Remove leading and trailing whitespace from a string.

    Args:
        s (str): The string to strip.

    Returns:
        str: The string with leading and trailing whitespace removed.
    """
    return s.strip()

def validate_ip_address(ip_address: str) -> bool:
    """
    Validate an IP address.

    Args:
        ip_address (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_regex, ip_address))

def truncate_string(s: str, max_length: int) -> str:
    """
    Truncate a string to a maximum length.

    Args:
        s (str): The string to truncate.
        max_length (int): The maximum length of the string.

    Returns:
        str: The truncated string.
    """
    if len(s) > max_length:
        return s[:max_length] + "..."
    return s
```
