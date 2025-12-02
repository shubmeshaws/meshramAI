```python
import re
import ipaddress
from typing import Any

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


def validate_ip_address(ip: str) -> bool:
    """
    Validate an IP address.

    Args:
        ip (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def validate_string_length(input_str: str, min_length: int = 1, max_length: int = None) -> bool:
    """
    Validate the length of a string.

    Args:
        input_str (str): The input string to validate.
        min_length (int, optional): The minimum allowed length. Defaults to 1.
        max_length (int, optional): The maximum allowed length. Defaults to None.

    Returns:
        bool: True if the string length is valid, False otherwise.
    """
    if max_length is not None and len(input_str) > max_length:
        return False
    return len(input_str) >= min_length


def validate_value_in_list(input_value: Any, allowed_values: list) -> bool:
    """
    Validate if a value is in a list of allowed values.

    Args:
        input_value (Any): The input value to validate.
        allowed_values (list): The list of allowed values.

    Returns:
        bool: True if the value is in the list, False otherwise.
    """
    return input_value in allowed_values


def validate_non_empty_list(input_list: list) -> bool:
    """
    Validate if a list is not empty.

    Args:
        input_list (list): The input list to validate.

    Returns:
        bool: True if the list is not empty, False otherwise.
    """
    return len(input_list) > 0
```
