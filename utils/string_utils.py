```python
"""
String utility functions.

This module provides functions to validate, format, and parse strings.
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
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def format_string(input_str: str, **kwargs) -> str:
    """
    Format a string with keyword arguments.

    Args:
    input_str (str): The string to format.
    **kwargs: Keyword arguments to replace in the string.

    Returns:
    str: The formatted string.
    """
    return input_str.format(**kwargs)

def parse_url(url: str) -> dict:
    """
    Parse a URL into its components.

    Args:
    url (str): The URL to parse.

    Returns:
    dict: A dictionary containing the URL's components (scheme, netloc, path, params, query, fragment).
    """
    from urllib.parse import urlparse
    return urlparse(url)._asdict()

def remove_special_chars(input_str: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_str (str): The string to remove special characters from.

    Returns:
    str: The string without special characters.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_str)

def truncate_string(input_str: str, max_length: int) -> str:
    """
    Truncate a string to a maximum length.

    Args:
    input_str (str): The string to truncate.
    max_length (int): The maximum length of the string.

    Returns:
    str: The truncated string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + '...'
    return input_str
```
