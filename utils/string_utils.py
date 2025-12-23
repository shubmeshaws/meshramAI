```python
"""
This module provides utility functions for string manipulation and validation.
"""

import re

def is_valid_email(email: str) -> bool:
    """
    Check if a given string is a valid email address.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def is_valid_ip_address(ip_address: str) -> bool:
    """
    Check if a given string is a valid IP address.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_regex, ip_address))

def remove_special_characters(input_string: str) -> str:
    """
    Remove special characters from a given string.

    Args:
    input_string (str): The string to remove special characters from.

    Returns:
    str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a given string to a specified maximum length.

    Args:
    input_string (str): The string to truncate.
    max_length (int): The maximum length of the output string.

    Returns:
    str: The input string truncated to the specified maximum length.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    else:
        return input_string
```
