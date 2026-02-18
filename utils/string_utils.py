```python
"""
Utility module for common string operations.

This module provides functions for validating, formatting, and manipulating strings.
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
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def format_string(input_str: str, max_length: int = 50) -> str:
    """
    Format a string to a specified maximum length.

    Args:
    input_str (str): The input string to format.
    max_length (int): The maximum length of the formatted string. Defaults to 50.

    Returns:
    str: The formatted string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length - 3] + "..."
    return input_str

def remove_special_chars(input_str: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_str (str): The input string to remove special characters from.

    Returns:
    str: The string with special characters removed.
    """
    return re.sub(r"[^a-zA-Z0-9\s]", "", input_str)

def camel_case_to_snake_case(input_str: str) -> str:
    """
    Convert a camel case string to snake case.

    Args:
    input_str (str): The input string to convert.

    Returns:
    str: The converted string in snake case.
    """
    return re.sub(r"([A-Z])", r"_\1", input_str).lower().lstrip("_")
```
