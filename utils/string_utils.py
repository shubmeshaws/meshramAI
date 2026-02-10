```python
"""
String utility functions.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if a given string is empty or contains only whitespace characters.

    Args:
    input_string (str): The string to be checked.

    Returns:
    bool: True if the string is empty, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validates an email address using a regular expression.

    Args:
    email (str): The email address to be validated.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def remove_special_chars(input_string: str) -> str:
    """
    Removes special characters from a given string.

    Args:
    input_string (str): The string from which special characters are to be removed.

    Returns:
    str: The string without special characters.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates a given string to a specified maximum length.

    Args:
    input_string (str): The string to be truncated.
    max_length (int): The maximum length of the string.

    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string
```
