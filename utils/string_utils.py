```python
"""
Utility functions for string manipulation and validation.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Check if a string is empty or contains only whitespace characters.

    Args:
    input_string (str): The input string to check.

    Returns:
    bool: True if the string is empty or contains only whitespace characters, False otherwise.
    """
    return not input_string.strip()


def validate_email(email: str) -> bool:
    """
    Validate an email address using a regular expression.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))


def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
    input_string (str): The input string to truncate.
    max_length (int): The maximum length of the output string.

    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string


def remove_special_characters(input_string: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_string (str): The input string to clean.

    Returns:
    str: The cleaned string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9\s]+', '', input_string)


def camel_case_to_snake_case(input_string: str) -> str:
    """
    Convert a camel case string to snake case.

    Args:
    input_string (str): The input string to convert.

    Returns:
    str: The converted string in snake case.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_string).lower()
```
