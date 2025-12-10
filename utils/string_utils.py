```python
"""
This module provides utility functions for string manipulation.
"""

import re

def camel_case_to_snake_case(input_str):
    """
    Converts a camel case string to snake case.

    Args:
        input_str (str): The input string in camel case.

    Returns:
        str: The input string converted to snake case.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_str).lower()

def validate_email(email):
    """
    Validates an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(email_regex, email))

def truncate_string(input_str, max_length):
    """
    Truncates a string to a specified maximum length.

    Args:
        input_str (str): The input string to truncate.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The truncated string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + '...'
    return input_str

def strip_whitespace(input_str):
    """
    Removes leading and trailing whitespace from a string.

    Args:
        input_str (str): The input string to strip.

    Returns:
        str: The input string with leading and trailing whitespace removed.
    """
    return input_str.strip()
```
