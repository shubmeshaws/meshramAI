```python
"""
Utility functions for string operations.
"""

import re

def is_valid_email(email: str) -> bool:
    """
    Checks if the given email is valid.
    
    Args:
    email (str): The email to validate.
    
    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def is_valid_ip(ip: str) -> bool:
    """
    Checks if the given IP address is valid.
    
    Args:
    ip (str): The IP address to validate.
    
    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_regex, ip))

def remove_special_chars(input_str: str) -> str:
    """
    Removes special characters from the given string.
    
    Args:
    input_str (str): The string to remove special characters from.
    
    Returns:
    str: The string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_str)

def truncate_string(input_str: str, max_length: int) -> str:
    """
    Truncates the given string to the specified maximum length.
    
    Args:
    input_str (str): The string to truncate.
    max_length (int): The maximum length of the string.
    
    Returns:
    str: The truncated string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + "..."
    return input_str
```
