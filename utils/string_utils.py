```python
"""
String utility module.

Provides functions for string manipulation and validation.
"""

import re

def is_empty(string: str) -> bool:
    """
    Checks if a string is empty.

    Args:
        string (str): The input string.

    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return not string.strip()

def validate_email(email: str) -> bool:
    """
    Validates an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def remove_special_chars(string: str) -> str:
    """
    Removes special characters from a string.

    Args:
        string (str): The input string.

    Returns:
        str: The string with special characters removed.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', string)

def truncate_string(string: str, max_length: int) -> str:
    """
    Truncates a string to a specified length.

    Args:
        string (str): The input string.
        max_length (int): The maximum length of the string.

    Returns:
        str: The truncated string.
    """
    if len(string) > max_length:
        return string[:max_length] + "..."
    return string
```
