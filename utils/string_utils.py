```python
"""
This module provides utility functions for string manipulation and validation.
"""

import re

def is_valid_email(email: str) -> bool:
    """
    Checks if the provided email is valid.

    Args:
        email (str): The email to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def is_valid_ip_address(ip_address: str) -> bool:
    """
    Checks if the provided IP address is valid.

    Args:
        ip_address (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_regex, ip_address))

def snake_case_to_camel_case(snake_case_string: str) -> str:
    """
    Converts a snake case string to camel case.

    Args:
        snake_case_string (str): The snake case string to convert.

    Returns:
        str: The camel case version of the input string.
    """
    components = snake_case_string.split("_")
    return components[0] + "".join(x.title() for x in components[1:])

def camel_case_to_snake_case(camel_case_string: str) -> str:
    """
    Converts a camel case string to snake case.

    Args:
        camel_case_string (str): The camel case string to convert.

    Returns:
        str: The snake case version of the input string.
    """
    snake_case_string = "".join(["_" + i.lower() if i.isupper() else i for i in camel_case_string]).lstrip("_")
    return snake_case_string
```
