```python
"""
String utility functions.

This module provides functions for common string operations such as validation and formatting.
"""

import re

def validate_input_string(input_str, min_length=1, max_length=255):
    """
    Validate an input string.

    Args:
        input_str (str): The input string to validate.
        min_length (int): The minimum allowed length (default: 1).
        max_length (int): The maximum allowed length (default: 255).

    Returns:
        bool: True if the input string is valid, False otherwise.
    """
    if not isinstance(input_str, str):
        return False
    if len(input_str) < min_length or len(input_str) > max_length:
        return False
    return True

def format_string_to_title_case(input_str):
    """
    Format a string to title case.

    Args:
        input_str (str): The input string to format.

    Returns:
        str: The formatted string in title case.
    """
    return input_str.title()

def validate_email_address(email_address):
    """
    Validate an email address.

    Args:
        email_address (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email_address))

def truncate_string(input_str, max_length=255):
    """
    Truncate a string to a specified maximum length.

    Args:
        input_str (str): The input string to truncate.
        max_length (int): The maximum allowed length (default: 255).

    Returns:
        str: The truncated string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length - 3] + "..."
    return input_str
```
