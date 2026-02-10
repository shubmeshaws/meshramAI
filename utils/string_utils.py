```python
"""
Utilities for string manipulation and validation.
"""

import re

def is_valid_ip_address(ip_address: str) -> bool:
    """
    Check if the given string is a valid IP address.

    Args:
        ip_address (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    ip_address_pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_pattern, ip_address))

def is_valid_dns_name(name: str) -> bool:
    """
    Check if the given string is a valid DNS name.

    Args:
        name (str): The DNS name to validate.

    Returns:
        bool: True if the DNS name is valid, False otherwise.
    """
    dns_name_pattern = r"^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$"
    return bool(re.match(dns_name_pattern, name, re.IGNORECASE))

def escape_special_characters(input_string: str) -> str:
    """
    Escape special characters in the given string.

    Args:
        input_string (str): The string to escape.

    Returns:
        str: The escaped string.
    """
    return input_string.replace("'", "\\'").replace('"', '\\"').replace(';', '\\;')

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate the given string to the specified maximum length.

    Args:
        input_string (str): The string to truncate.
        max_length (int): The maximum length of the string.

    Returns:
        str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string
```
