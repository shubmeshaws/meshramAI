```python
import re
from typing import Any, Dict, List

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


def validate_ip_address(ip_address: str) -> bool:
    """
    Validate an IP address.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_regex, ip_address))


def validate_port(port: int) -> bool:
    """
    Validate a port number.

    Args:
    port (int): The port number to validate.

    Returns:
    bool: True if the port number is valid, False otherwise.
    """
    return 0 <= port <= 65535


def validate_dict_keys(dictionary: Dict[str, Any], required_keys: List[str]) -> bool:
    """
    Validate if a dictionary contains all required keys.

    Args:
    dictionary (Dict[str, Any]): The dictionary to validate.
    required_keys (List[str]): The required keys.

    Returns:
    bool: True if the dictionary contains all required keys, False otherwise.
    """
    return all(key in dictionary for key in required_keys)


def validate_dict_values(dictionary: Dict[str, Any], key: str, value_type: type) -> bool:
    """
    Validate the type of a dictionary value.

    Args:
    dictionary (Dict[str, Any]): The dictionary to validate.
    key (str): The key to check.
    value_type (type): The expected type of the value.

    Returns:
    bool: True if the value is of the expected type, False otherwise.
    """
    return key in dictionary and isinstance(dictionary[key], value_type)
```
