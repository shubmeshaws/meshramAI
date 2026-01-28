```python
"""
This module provides general string utility functions.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if a given string is empty or contains only whitespace characters.

    Args:
    input_string (str): The input string to check.

    Returns:
    bool: True if the string is empty, False otherwise.
    """
    return not input_string.strip()

def validate_email(input_string: str) -> bool:
    """
    Validates an email address.

    Args:
    input_string (str): The input string to validate.

    Returns:
    bool: True if the string is a valid email address, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, input_string))

def remove_special_chars(input_string: str) -> str:
    """
    Removes special characters from a given string.

    Args:
    input_string (str): The input string to remove special characters from.

    Returns:
    str: The string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates a given string to a specified maximum length.

    Args:
    input_string (str): The input string to truncate.
    max_length (int): The maximum length of the string.

    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string
```
