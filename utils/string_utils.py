```python
# utils/string_utils.py

"""
Utility functions for string manipulation and validation.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if a string is empty or contains only whitespace characters.

    Args:
    input_string (str): The input string to be checked.

    Returns:
    bool: True if the string is empty or contains only whitespace characters, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validates an email address using a regular expression.

    Args:
    email (str): The email address to be validated.

    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates a string to a specified maximum length.

    Args:
    input_string (str): The input string to be truncated.
    max_length (int): The maximum length of the output string.

    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string

def camel_case_to_snake_case(input_string: str) -> str:
    """
    Converts a camel case string to snake case.

    Args:
    input_string (str): The input string to be converted.

    Returns:
    str: The converted string in snake case.
    """
    snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', input_string).lower()
    return snake_case_string
```
