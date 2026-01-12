```python
"""
String utility module.

This module provides functions for string manipulation and validation.
"""

import re

def is_empty(string):
    """
    Check if a string is empty.

    Args:
        string (str): The input string.

    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return not string.strip()

def validate_email(email):
    """
    Validate an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def snake_to_camel_case(snake_case_string):
    """
    Convert a snake case string to camel case.

    Args:
        snake_case_string (str): The input string in snake case.

    Returns:
        str: The input string in camel case.
    """
    words = snake_case_string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])

def camel_to_snake_case(camel_case_string):
    """
    Convert a camel case string to snake case.

    Args:
        camel_case_string (str): The input string in camel case.

    Returns:
        str: The input string in snake case.
    """
    snake_case_string = ""
    for char in camel_case_string:
        if char.isupper():
            snake_case_string += "_" + char.lower()
        else:
            snake_case_string += char
    return snake_case_string
```
