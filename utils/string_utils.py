```python
"""
Utility file for handling string operations.
"""

import re

def is_valid_ip(ip_address: str) -> bool:
    """
    Validate if the given string is a valid IP address.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(pattern, ip_address))

def is_valid_hostname(hostname: str) -> bool:
    """
    Validate if the given string is a valid hostname.

    Args:
    hostname (str): The hostname to validate.

    Returns:
    bool: True if the hostname is valid, False otherwise.
    """
    pattern = r"^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$"
    return bool(re.match(pattern, hostname))

def remove_special_chars(input_str: str) -> str:
    """
    Remove special characters from a given string.

    Args:
    input_str (str): The input string.

    Returns:
    str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_str)

def truncate_string(input_str: str, max_length: int) -> str:
    """
    Truncate a given string to a specified maximum length.

    Args:
    input_str (str): The input string.
    max_length (int): The maximum length of the output string.

    Returns:
    str: The input string truncated to the specified maximum length.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + "..."
    return input_str
```
