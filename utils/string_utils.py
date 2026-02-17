```python
"""
Utility functions for handling string operations.
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
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def validate_ip_address(ip_address: str) -> bool:
    """
    Validate an IP address.
    
    Args:
        ip_address (str): The IP address to validate.
    
    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_regex, ip_address))

def camel_case_to_snake_case(camel_case_string: str) -> str:
    """
    Convert a camel case string to snake case.
    
    Args:
        camel_case_string (str): The camel case string to convert.
    
    Returns:
        str: The snake case version of the input string.
    """
    snake_case_string = re.sub("([A-Z])", r"_\1", camel_case_string).lower()
    return snake_case_string.lstrip("_")

def snake_case_to_camel_case(snake_case_string: str) -> str:
    """
    Convert a snake case string to camel case.
    
    Args:
        snake_case_string (str): The snake case string to convert.
    
    Returns:
        str: The camel case version of the input string.
    """
    words = snake_case_string.split("_")
    camel_case_string = words[0] + "".join(word.capitalize() for word in words[1:])
    return camel_case_string
```
