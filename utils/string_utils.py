```python
"""
String Utilities
================

This module provides a set of functions for general string manipulation and validation.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Check if a string is empty or contains only whitespace.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the string is empty or contains only whitespace, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validate an email address using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def extract_numbers(input_string: str) -> list[int]:
    """
    Extract all numbers from a string.

    Args:
        input_string (str): The input string to extract numbers from.

    Returns:
        list[int]: A list of extracted numbers.
    """
    return [int(num) for num in re.findall(r"\d+", input_string)]

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
        input_string (str): The input string to truncate.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string
```
