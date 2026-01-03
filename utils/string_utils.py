```python
"""
String utility functions.

This module provides a set of functions to handle string operations, including validation, sanitization, and formatting.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def sanitize_string(input_string: str) -> str:
    """
    Sanitize a string by removing special characters and leading/trailing whitespaces.

    Args:
    input_string (str): The string to sanitize.

    Returns:
    str: The sanitized string.
    """
    sanitized_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
    return sanitized_string.strip()

def format_string(input_string: str, **kwargs) -> str:
    """
    Format a string using keyword arguments.

    Args:
    input_string (str): The string to format.
    **kwargs: Keyword arguments to use for formatting.

    Returns:
    str: The formatted string.
    """
    return input_string.format(**kwargs)

def convert_to_slug(input_string: str) -> str:
    """
    Convert a string to a slug (lowercase, hyphen-separated).

    Args:
    input_string (str): The string to convert.

    Returns:
    str: The converted slug.
    """
    slug = input_string.lower().replace(' ', '-')
    return re.sub(r'[^a-z0-9-]', '', slug)
```
