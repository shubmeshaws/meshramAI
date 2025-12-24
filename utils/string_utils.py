```python
"""
String utility functions for general string manipulation.

This module provides functions for string validation, formatting, and manipulation.
It can be used throughout the project to handle various string inputs and outputs.
"""

import re

def is_valid_ip_address(ip_address: str) -> bool:
    """
    Validate if the given string is a valid IP address.

    Args:
        ip_address (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    ip_address_pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_pattern, ip_address))

def is_valid_hostname(hostname: str) -> bool:
    """
    Validate if the given string is a valid hostname.

    Args:
        hostname (str): The hostname to validate.

    Returns:
        bool: True if the hostname is valid, False otherwise.
    """
    hostname_pattern = r"^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$"
    return bool(re.match(hostname_pattern, hostname))

def camel_case_to_snake_case(input_string: str) -> str:
    """
    Convert a camel case string to snake case.

    Args:
        input_string (str): The string to convert.

    Returns:
        str: The input string in snake case.
    """
    snake_case_string = re.sub(r"([A-Z])", r"_\1", input_string).lower()
    return snake_case_string.lstrip("_")

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
        input_string (str): The string to truncate.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The input string truncated to the specified maximum length.
    """
    if len(input_string) > max_length:
        return input_string[:max_length - 3] + "..."
    return input_string
```
