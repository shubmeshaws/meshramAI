```python
"""
String Utilities Module
========================
This module contains functions for string manipulation and validation.
"""

import re

def is_empty(string):
    """
    Checks if a string is empty.

    Args:
        string (str): The input string.

    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return not string.strip()

def validate_email(email):
    """
    Validates an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def snake_case_to_camel_case(string):
    """
    Converts a snake_case string to camelCase.

    Args:
        string (str): The input string.

    Returns:
        str: The camelCase equivalent of the input string.
    """
    words = string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])

def camel_case_to_snake_case(string):
    """
    Converts a camelCase string to snake_case.

    Args:
        string (str): The input string.

    Returns:
        str: The snake_case equivalent of the input string.
    """
    snake_case = ""
    for i, char in enumerate(string):
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

def truncate_string(string, length):
    """
    Truncates a string to a specified length.

    Args:
        string (str): The input string.
        length (int): The desired length.

    Returns:
        str: The truncated string.
    """
    if len(string) > length:
        return string[:length] + "..."
    return string
```
