```python
# utils/string_utils.py

"""
Utility module for common string operations.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if a string is empty or contains only whitespace characters.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the string is empty, False otherwise.
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
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def sanitize_string(input_string: str) -> str:
    """
    Sanitizes a string by removing special characters and converting to lowercase.

    Args:
        input_string (str): The input string to sanitize.

    Returns:
        str: The sanitized string.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string).lower()

def format_string(input_string: str, **kwargs) -> str:
    """
    Formats a string using keyword arguments.

    Args:
        input_string (str): The input string to format.
        **kwargs: Keyword arguments to replace placeholders in the string.

    Returns:
        str: The formatted string.
    """
    return input_string.format(**kwargs)
```
