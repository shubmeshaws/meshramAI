```python
"""
String utility module for string manipulation and validation.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if a string is empty.

    Args:
    input_string (str): The input string to check.

    Returns:
    bool: True if the string is empty, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validates an email address.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def validate_ip_address(ip_address: str) -> bool:
    """
    Validates an IP address.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_regex, ip_address))

def camel_case_to_snake_case(input_string: str) -> str:
    """
    Converts a camel case string to snake case.

    Args:
    input_string (str): The input string to convert.

    Returns:
    str: The input string in snake case.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_string).lower()
```
