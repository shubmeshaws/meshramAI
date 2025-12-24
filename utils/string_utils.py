```python
"""
String utility functions.

This module contains functions for string manipulation and validation.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if a string is empty or contains only whitespace.

    Args:
    input_string (str): The string to check.

    Returns:
    bool: True if the string is empty or contains only whitespace, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validates an email address.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def truncate_string(long_string: str, max_length: int) -> str:
    """
    Truncates a string to a specified length.

    Args:
    long_string (str): The string to truncate.
    max_length (int): The maximum length of the truncated string.

    Returns:
    str: The truncated string.
    """
    if len(long_string) > max_length:
        return long_string[:max_length - 3] + "..."
    return long_string

def remove_special_chars(input_string: str) -> str:
    """
    Removes special characters from a string.

    Args:
    input_string (str): The string to clean.

    Returns:
    str: The string without special characters.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)
```
