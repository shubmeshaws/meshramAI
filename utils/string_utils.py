```python
"""
String utility functions.
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

def format_string(input_string: str, **kwargs) -> str:
    """
    Format a string using keyword arguments.

    Args:
    input_string (str): The input string to format.
    **kwargs: Keyword arguments to replace in the input string.

    Returns:
    str: The formatted string.
    """
    return input_string.format(**kwargs)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a maximum length.

    Args:
    input_string (str): The input string to truncate.
    max_length (int): The maximum length of the output string.

    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string
```
