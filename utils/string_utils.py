```python
"""
Utility functions for string manipulation and validation.
"""

import re

def is_valid_email(email: str) -> bool:
    """
    Checks if the given email is valid.
    
    Args:
    email (str): The email to be validated.
    
    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def validate_ip_address(ip: str) -> bool:
    """
    Checks if the given IP address is valid.
    
    Args:
    ip (str): The IP address to be validated.
    
    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_regex, ip))

def remove_special_chars(input_str: str) -> str:
    """
    Removes all special characters from the given string.
    
    Args:
    input_str (str): The string from which special characters are to be removed.
    
    Returns:
    str: The string without special characters.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_str)

def camel_case_to_snake_case(input_str: str) -> str:
    """
    Converts a camel case string to snake case.
    
    Args:
    input_str (str): The camel case string to be converted.
    
    Returns:
    str: The snake case equivalent of the input string.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_str).lower()
```
