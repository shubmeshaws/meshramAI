```python
"""
String utility functions.

This module provides functions for string manipulation and validation.
"""

import re

def is_empty(string: str) -> bool:
    """
    Check if a string is empty or contains only whitespace characters.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return not string.strip()

def is_alphanumeric(string: str) -> bool:
    """
    Check if a string contains only alphanumeric characters.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is alphanumeric, False otherwise.
    """
    return re.match("^[a-zA-Z0-9]+$", string) is not None

def is_email(string: str) -> bool:
    """
    Check if a string is a valid email address.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is a valid email address, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_regex, string) is not None

def truncate_string(string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
        string (str): The string to truncate.
        max_length (int): The maximum length of the string.

    Returns:
        str: The truncated string.
    """
    if len(string) > max_length:
        return string[:max_length - 3] + "..."
    return string

def remove_special_chars(string: str) -> str:
    """
    Remove special characters from a string.

    Args:
        string (str): The string to remove special characters from.

    Returns:
        str: The string with special characters removed.
    """
    return re.sub(r"[^a-zA-Z0-9\s]", "", string)
```
