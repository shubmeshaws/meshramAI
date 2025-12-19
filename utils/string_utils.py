```python
"""
String utility functions.

This module provides a set of functions for common string operations, including
validation, sanitization, and formatting.
"""

import re

def is_valid_ip_address(ip_address: str) -> bool:
    """
    Validate an IP address.

    Args:
        ip_address (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    ip_address_pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_pattern, ip_address))

def sanitize_string(input_string: str) -> str:
    """
    Sanitize a string by removing special characters and whitespace.

    Args:
        input_string (str): The string to sanitize.

    Returns:
        str: The sanitized string.
    """
    return re.sub(r"[^a-zA-Z0-9]", "", input_string)

def format_string(input_string: str, **kwargs) -> str:
    """
    Format a string using keyword arguments.

    Args:
        input_string (str): The string to format.
        **kwargs: Keyword arguments to use for formatting.

    Returns:
        str: The formatted string.
    """
    return input_string.format(**kwargs)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
        input_string (str): The string to truncate.
        max_length (int): The maximum length of the string.

    Returns:
        str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length - 3] + "..."
    return input_string
```
