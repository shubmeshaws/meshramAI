```python
"""
String utility functions for common operations.
"""

import re

def is_valid_ipv4(ip_address: str) -> bool:
    """
    Validate an IPv4 address.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(pattern, ip_address))

def is_valid_ipv6(ip_address: str) -> bool:
    """
    Validate an IPv6 address.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    pattern = r"^([a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}$"
    return bool(re.match(pattern, ip_address))

def validate_hostname(hostname: str) -> bool:
    """
    Validate a hostname.

    Args:
    hostname (str): The hostname to validate.

    Returns:
    bool: True if the hostname is valid, False otherwise.
    """
    pattern = r"^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$"
    return bool(re.match(pattern, hostname))

def remove_special_chars(input_string: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_string (str): The string to clean.

    Returns:
    str: The cleaned string.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a specified length.

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
