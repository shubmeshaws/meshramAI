```python
# utils/string_utils.py

import re

def is_valid_ipv4_address(ip_address: str) -> bool:
    """
    Validate if a given string is a valid IPv4 address.
    
    Args:
    ip_address (str): The IP address to validate.
    
    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ipv4_pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ipv4_pattern, ip_address))

def is_valid_ipv6_address(ip_address: str) -> bool:
    """
    Validate if a given string is a valid IPv6 address.
    
    Args:
    ip_address (str): The IP address to validate.
    
    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ipv6_pattern = r"^([a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}$"
    return bool(re.match(ipv6_pattern, ip_address))

def validate_string_length(input_string: str, min_length: int, max_length: int) -> bool:
    """
    Validate if a given string length is within a specified range.
    
    Args:
    input_string (str): The input string to validate.
    min_length (int): The minimum allowed length.
    max_length (int): The maximum allowed length.
    
    Returns:
    bool: True if the string length is within the specified range, False otherwise.
    """
    return min_length <= len(input_string) <= max_length

def remove_special_characters(input_string: str) -> str:
    """
    Remove special characters from a given string.
    
    Args:
    input_string (str): The input string to process.
    
    Returns:
    str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)
```
