```python
"""
String utility functions for various string operations.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if the input string is empty or None.

    Args:
    input_string (str): The input string to check.

    Returns:
    bool: True if the input string is empty or None, False otherwise.
    """
    return input_string is None or input_string.strip() == ""

def validate_email(input_string: str) -> bool:
    """
    Validates if the input string is a valid email address.

    Args:
    input_string (str): The input string to validate.

    Returns:
    bool: True if the input string is a valid email address, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, input_string))

def remove_special_characters(input_string: str) -> str:
    """
    Removes special characters from the input string.

    Args:
    input_string (str): The input string to clean.

    Returns:
    str: The input string without special characters.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

def truncate_string(input_string: str, length: int) -> str:
    """
    Truncates the input string to the specified length.

    Args:
    input_string (str): The input string to truncate.
    length (int): The desired length of the output string.

    Returns:
    str: The truncated input string.
    """
    if len(input_string) > length:
        return input_string[:length] + "..."
    return input_string
```
