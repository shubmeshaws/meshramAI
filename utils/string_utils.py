```python
"""
Utility module for string manipulation and validation.
"""

import re

def is_valid_ip_address(ip_address: str) -> bool:
    """
    Validate if a given string is a valid IP address.
    
    Args:
    ip_address (str): The IP address to validate.
    
    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_regex, ip_address))


def is_valid_hostname(hostname: str) -> bool:
    """
    Validate if a given string is a valid hostname.
    
    Args:
    hostname (str): The hostname to validate.
    
    Returns:
    bool: True if the hostname is valid, False otherwise.
    """
    hostname_regex = r"^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$"
    return bool(re.match(hostname_regex, hostname))


def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a given string to a specified maximum length.
    
    Args:
    input_string (str): The string to truncate.
    max_length (int): The maximum length of the output string.
    
    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length - 3] + "..."
    return input_string


def remove_special_characters(input_string: str) -> str:
    """
    Remove all special characters from a given string.
    
    Args:
    input_string (str): The string to clean.
    
    Returns:
    str: The cleaned string.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
```
