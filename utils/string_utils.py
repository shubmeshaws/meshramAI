```python
"""
This module provides utility functions for string manipulation and validation.
"""

import re

def is_valid_email(email: str) -> bool:
    """
    Checks if the given email address is valid.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def is_valid_ip_address(ip_address: str) -> bool:
    """
    Checks if the given IP address is valid.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_regex, ip_address))

def remove_special_characters(input_string: str) -> str:
    """
    Removes special characters from the given input string.

    Args:
    input_string (str): The string from which to remove special characters.

    Returns:
    str: The input string with special characters removed.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates the given input string to the specified maximum length.

    Args:
    input_string (str): The string to truncate.
    max_length (int): The maximum length of the truncated string.

    Returns:
    str: The truncated input string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string
```
