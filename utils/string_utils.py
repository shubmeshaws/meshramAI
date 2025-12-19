```python
"""
This module provides common string utility functions.
"""

import re
import ipaddress

def to_title_case(input_string):
    """
    Converts a string to title case.

    Args:
        input_string (str): The string to convert.

    Returns:
        str: The input string in title case.
    """
    return input_string.title()

def is_valid_ip_address(ip_address):
    """
    Checks if a string is a valid IP address.

    Args:
        ip_address (str): The string to check.

    Returns:
        bool: True if the string is a valid IP address, False otherwise.
    """
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False

def is_valid_domain_name(domain_name):
    """
    Checks if a string is a valid domain name.

    Args:
        domain_name (str): The string to check.

    Returns:
        bool: True if the string is a valid domain name, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z]{2,})+$"
    return bool(re.match(pattern, domain_name))

def truncate_string(input_string, max_length):
    """
    Truncates a string to a maximum length.

    Args:
        input_string (str): The string to truncate.
        max_length (int): The maximum length of the string.

    Returns:
        str: The input string truncated to the maximum length.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string
```
