```python
"""
This module provides utility functions for handling string operations.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if a given string is empty.

    Args:
    input_string (str): The string to check.

    Returns:
    bool: True if the string is empty, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validates an email address using a regular expression.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def compare_strings(str1: str, str2: str) -> bool:
    """
    Compares two strings ignoring case and leading/trailing whitespace.

    Args:
    str1 (str): The first string to compare.
    str2 (str): The second string to compare.

    Returns:
    bool: True if the strings are equal, False otherwise.
    """
    return str1.strip().casefold() == str2.strip().casefold()

def format_string(input_string: str, **kwargs) -> str:
    """
    Formats a string using keyword arguments.

    Args:
    input_string (str): The string to format.
    **kwargs: Keyword arguments to replace in the string.

    Returns:
    str: The formatted string.
    """
    return input_string.format(**kwargs)
```
