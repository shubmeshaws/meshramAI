```python
"""
String utility functions.
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
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
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

def extract_numbers(input_string: str) -> list[int]:
    """
    Extract numbers from a string.

    Args:
    input_string (str): The string to extract numbers from.

    Returns:
    list[int]: A list of extracted numbers.
    """
    return [int(num) for num in re.findall(r"\d+", input_string)]

def camel_case_to_snake_case(input_string: str) -> str:
    """
    Convert a camel case string to snake case.

    Args:
    input_string (str): The string to convert.

    Returns:
    str: The converted string.
    """
    return re.sub(r"([A-Z])", r"_\1", input_string).lower().lstrip("_")
```
