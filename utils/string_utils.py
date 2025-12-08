```python
"""
Utility functions for common string operations.
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

def is_valid_domain_name(domain_name: str) -> bool:
    """
    Validate if the given string is a valid domain name.

    Args:
    domain_name (str): The domain name to validate.

    Returns:
    bool: True if the domain name is valid, False otherwise.
    """
    domain_name_pattern = r"^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$"
    return bool(re.match(domain_name_pattern, domain_name))

def sanitize_string(input_string: str) -> str:
    """
    Remove leading and trailing whitespace from the input string.

    Args:
    input_string (str): The string to sanitize.

    Returns:
    str: The sanitized string.
    """
    return input_string.strip()

def is_string_empty(input_string: str) -> bool:
    """
    Check if the input string is empty or contains only whitespace.

    Args:
    input_string (str): The string to check.

    Returns:
    bool: True if the string is empty, False otherwise.
    """
    return not input_string.strip()

def extract_substring(input_string: str, start_pattern: str, end_pattern: str) -> str:
    """
    Extract a substring from the input string based on the given start and end patterns.

    Args:
    input_string (str): The string to extract from.
    start_pattern (str): The pattern to match the start of the substring.
    end_pattern (str): The pattern to match the end of the substring.

    Returns:
    str: The extracted substring.
    """
    start_index = input_string.find(start_pattern)
    if start_index == -1:
        return ""
    end_index = input_string.find(end_pattern, start_index + len(start_pattern))
    if end_index == -1:
        return ""
    return input_string[start_index + len(start_pattern):end_index]
```
