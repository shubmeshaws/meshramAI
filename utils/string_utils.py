```python
"""
Utility functions for string manipulation and validation.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if the input string is empty or contains only whitespace characters.

    Args:
    input_string (str): The input string to check.

    Returns:
    bool: True if the input string is empty or contains only whitespace characters, False otherwise.
    """
    return input_string.strip() == ""

def validate_email(input_string: str) -> bool:
    """
    Validates if the input string is a valid email address.

    Args:
    input_string (str): The input string to validate.

    Returns:
    bool: True if the input string is a valid email address, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, input_string))

def validate_ipv4_address(input_string: str) -> bool:
    """
    Validates if the input string is a valid IPv4 address.

    Args:
    input_string (str): The input string to validate.

    Returns:
    bool: True if the input string is a valid IPv4 address, False otherwise.
    """
    ipv4_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ipv4_regex, input_string))

def remove_special_characters(input_string: str) -> str:
    """
    Removes special characters from the input string.

    Args:
    input_string (str): The input string to clean.

    Returns:
    str: The input string with special characters removed.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
```
