```python
"""
This module provides utility functions for string manipulation and validation.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if the input string is empty or contains only whitespace characters.

    Args:
    input_string (str): The input string to be checked.

    Returns:
    bool: True if the string is empty, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validates if the input string is a valid email address.

    Args:
    email (str): The input email address to be validated.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates the input string to the specified maximum length.

    Args:
    input_string (str): The input string to be truncated.
    max_length (int): The maximum length of the output string.

    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string

def remove_special_characters(input_string: str) -> str:
    """
    Removes all special characters from the input string.

    Args:
    input_string (str): The input string to be cleaned.

    Returns:
    str: The cleaned string without special characters.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)
```
