```python
"""
String utility functions.

This module provides various functions for working with strings, including validation, formatting, and manipulation.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Check if a string is empty or contains only whitespace characters.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the string is empty or contains only whitespace characters, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def format_string(input_string: str, **kwargs) -> str:
    """
    Format a string using keyword arguments.

    Args:
        input_string (str): The input string to format.
        **kwargs: Keyword arguments to use for formatting.

    Returns:
        str: The formatted string.
    """
    return input_string.format(**kwargs)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
        input_string (str): The input string to truncate.
        max_length (int): The maximum length of the truncated string.

    Returns:
        str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length - 3] + "..."
    return input_string

def remove_special_characters(input_string: str) -> str:
    """
    Remove special characters from a string.

    Args:
        input_string (str): The input string to clean.

    Returns:
        str: The cleaned string.
    """
    return re.sub(r"[^a-zA-Z0-9\s]", "", input_string)
```
