```python
"""
String utility functions.

This module provides functions for string manipulation and validation.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Check if the input string is empty.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return not input_string.strip()

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

def snake_case_to_camel_case(input_string: str) -> str:
    """
    Convert a snake case string to camel case.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: The input string converted to camel case.
    """
    words = input_string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a maximum length.

    Args:
        input_string (str): The input string to truncate.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The truncated input string.
    """
    if len(input_string) > max_length:
        return input_string[: max_length - 3] + "..."
    return input_string
```
