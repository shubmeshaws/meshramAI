```python
"""
String utility functions.

This module provides a collection of functions for string manipulation and validation.
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
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def snake_case_to_camel_case(snake_case_str: str) -> str:
    """
    Convert a snake_case string to camelCase.

    Args:
    snake_case_str (str): The string to convert.

    Returns:
    str: The camelCase equivalent of the input string.
    """
    components = snake_case_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])

def truncate_string(input_str: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
    input_str (str): The string to truncate.
    max_length (int): The maximum length of the output string.

    Returns:
    str: The truncated string.
    """
    if len(input_str) > max_length:
        return input_str[: max_length - 3] + "..."
    return input_str

def remove_special_chars(input_str: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_str (str): The string to clean.

    Returns:
    str: The input string with all special characters removed.
    """
    return re.sub(r"[^a-zA-Z0-9\s]", "", input_str)
```
