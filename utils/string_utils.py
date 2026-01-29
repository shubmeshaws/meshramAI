```python
"""
String utility module for string manipulation and validation.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate if the provided email is valid.

    Args:
    email (str): The email to validate.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def validate_ip_address(ip_address: str) -> bool:
    """
    Validate if the provided IP address is valid.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return bool(re.match(ip_address_regex, ip_address))

def extract_numbers(input_string: str) -> list:
    """
    Extract numbers from the provided string.

    Args:
    input_string (str): The string to extract numbers from.

    Returns:
    list: A list of extracted numbers.
    """
    return re.findall(r'\d+', input_string)

def remove_special_characters(input_string: str) -> str:
    """
    Remove special characters from the provided string.

    Args:
    input_string (str): The string to remove special characters from.

    Returns:
    str: The string without special characters.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
```
