```python
"""
String utility functions.

This module provides a set of functions for string manipulation and validation.
"""

import re

def is_empty_string(input_str):
    """
    Check if a string is empty or contains only whitespace.

    Args:
        input_str (str): The input string to check.

    Returns:
        bool: True if the string is empty or contains only whitespace, False otherwise.
    """
    return input_str.strip() == ""

def validate_email(email):
    """
    Validate an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def truncate_string(input_str, max_length):
    """
    Truncate a string to a specified maximum length.

    Args:
        input_str (str): The input string to truncate.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The truncated string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + "..."
    return input_str

def convert_to_snake_case(input_str):
    """
    Convert a string to snake case.

    Args:
        input_str (str): The input string to convert.

    Returns:
        str: The input string in snake case.
    """
    return re.sub(r"([A-Z])", r"_\1", input_str).lower().lstrip("_")
```
