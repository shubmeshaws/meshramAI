```python
"""
Utility functions for string manipulation and validation.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate an email address.
    
    Args:
    email (str): The email address to validate.
    
    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def validate_ip(ip: str) -> bool:
    """
    Validate an IP address.
    
    Args:
    ip (str): The IP address to validate.
    
    Returns:
    bool: True if the IP is valid, False otherwise.
    """
    ip_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_regex, ip))

def remove_special_chars(input_str: str) -> str:
    """
    Remove special characters from a string.
    
    Args:
    input_str (str): The string to remove special characters from.
    
    Returns:
    str: The string without special characters.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_str)

def convert_to_snake_case(input_str: str) -> str:
    """
    Convert a string to snake case.
    
    Args:
    input_str (str): The string to convert to snake case.
    
    Returns:
    str: The string in snake case.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_str).lower()
```
