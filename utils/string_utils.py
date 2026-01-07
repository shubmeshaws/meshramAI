```python
"""
String utility functions for general use.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if a string is empty or contains only whitespace.

    Args:
        input_string (str): The string to check.

    Returns:
        bool: True if the string is empty or contains only whitespace, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validates an email address using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates a string to a specified maximum length.

    Args:
        input_string (str): The string to truncate.
        max_length (int): The maximum length of the string.

    Returns:
        str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string

def remove_special_chars(input_string: str) -> str:
    """
    Removes special characters from a string.

    Args:
        input_string (str): The string to remove special characters from.

    Returns:
        str: The string with special characters removed.
    """
    return re.sub(r"[^a-zA-Z0-9\s]", "", input_string)

def title_case(input_string: str) -> str:
    """
    Converts a string to title case.

    Args:
        input_string (str): The string to convert.

    Returns:
        str: The string in title case.
    """
    return input_string.title()
```
