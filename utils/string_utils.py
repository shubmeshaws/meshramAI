```python
"""
String utility module for general string operations.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
    email (str): The email address to be validated.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def sanitize_string(input_string: str) -> str:
    """
    Sanitize a string by removing leading/trailing whitespaces and special characters.

    Args:
    input_string (str): The string to be sanitized.

    Returns:
    str: The sanitized string.
    """
    sanitized_string = input_string.strip()
    sanitized_string = re.sub(r'[^a-zA-Z0-9\s]', '', sanitized_string)
    return sanitized_string

def format_string(input_string: str, upper_case: bool = False) -> str:
    """
    Format a string by converting it to upper case or lower case.

    Args:
    input_string (str): The string to be formatted.
    upper_case (bool): Whether to convert the string to upper case. Defaults to False.

    Returns:
    str: The formatted string.
    """
    if upper_case:
        return input_string.upper()
    else:
        return input_string.lower()

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
    input_string (str): The string to be truncated.
    max_length (int): The maximum length of the string.

    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    else:
        return input_string
```
