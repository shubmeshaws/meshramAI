```python
"""
String utility module for common string operations.
"""

import re

def is_empty(string: str) -> bool:
    """
    Check if a string is empty or contains only whitespace.

    Args:
        string (str): The input string to check.

    Returns:
        bool: True if the string is empty or contains only whitespace, False otherwise.
    """
    return not string.strip()

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def truncate_string(string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
        string (str): The input string to truncate.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The truncated string.
    """
    if len(string) > max_length:
        return string[:max_length] + "..."
    return string

def remove_special_chars(string: str) -> str:
    """
    Remove special characters from a string.

    Args:
        string (str): The input string to clean.

    Returns:
        str: The cleaned string.
    """
    return re.sub(r"[^a-zA-Z0-9\s]", "", string)

def to_snake_case(string: str) -> str:
    """
    Convert a string to snake case.

    Args:
        string (str): The input string to convert.

    Returns:
        str: The converted string.
    """
    return re.sub(r"([A-Z])", r"_\1", string).lower().lstrip("_")
```
