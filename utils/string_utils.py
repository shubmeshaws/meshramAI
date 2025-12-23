```python
"""
String Utilities Module
========================
This module provides a set of functions for string manipulation, including text formatting and validation.
"""

import re

def truncate_string(input_str, max_length):
    """
    Truncates a string to a specified maximum length.

    Args:
        input_str (str): The input string to be truncated.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The truncated string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + "..."
    return input_str

def validate_email(email):
    """
    Validates an email address using a regular expression.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def remove_special_chars(input_str):
    """
    Removes special characters from a string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The string with special characters removed.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_str)

def capitalize_first_letter(input_str):
    """
    Capitalizes the first letter of a string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The string with the first letter capitalized.
    """
    return input_str.capitalize()
```
