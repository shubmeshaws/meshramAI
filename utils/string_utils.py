```python
"""
String Utilities Module
=======================

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
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def remove_special_chars(input_str: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_str (str): The input string.

    Returns:
    str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_str)

def truncate_string(input_str: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
    input_str (str): The input string.
    max_length (int): The maximum length.

    Returns:
    str: The truncated string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + "..."
    return input_str

def camel_case_to_snake_case(input_str: str) -> str:
    """
    Convert a camel case string to snake case.

    Args:
    input_str (str): The input string.

    Returns:
    str: The input string in snake case.
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
```
