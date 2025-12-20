```python
"""
This module provides common string utility functions for validation, formatting, and manipulation.
"""

import re

def is_valid_email(email: str) -> bool:
    """
    Validate if the provided string is a valid email address.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def is_valid_ip(ip: str) -> bool:
    """
    Validate if the provided string is a valid IP address.
    
    Args:
        ip (str): The IP address to validate.
    
    Returns:
        bool: True if the IP is valid, False otherwise.
    """
    ip_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_regex, ip))

def snake_to_camel(snake_str: str) -> str:
    """
    Convert a snake_case string to camelCase.
    
    Args:
        snake_str (str): The snake_case string to convert.
    
    Returns:
        str: The converted camelCase string.
    """
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])

def camel_to_snake(camel_str: str) -> str:
    """
    Convert a camelCase string to snake_case.
    
    Args:
        camel_str (str): The camelCase string to convert.
    
    Returns:
        str: The converted snake_case string.
    """
    snake_str = "".join(["_" + i.lower() if i.isupper() else i for i in camel_str]).lstrip("_")
    return snake_str
```
