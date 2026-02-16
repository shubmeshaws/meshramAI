```python
"""
String utility functions.

This module provides functions for string manipulation and validation.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if a string is empty or contains only whitespace characters.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the string is empty or contains only whitespace characters, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validates an email address using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def remove_special_characters(input_string: str) -> str:
    """
    Removes special characters from a string.

    Args:
        input_string (str): The input string to process.

    Returns:
        str: The input string with special characters removed.
    """
    return re.sub(r"[^a-zA-Z0-9\s]", "", input_string)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates a string to a specified maximum length.

    Args:
        input_string (str): The input string to truncate.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The input string truncated to the specified maximum length.
    """
    if len(input_string) > max_length:
        return input_string[:max_length - 3] + "..."
    return input_string
```
