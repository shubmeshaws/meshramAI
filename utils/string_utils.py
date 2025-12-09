```python
# utils/string_utils.py

import re

def is_valid_ip_address(ip_address: str) -> bool:
    """
    Validate an IP address.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_address_pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_pattern, ip_address))

def is_valid_domain_name(domain_name: str) -> bool:
    """
    Validate a domain name.

    Args:
    domain_name (str): The domain name to validate.

    Returns:
    bool: True if the domain name is valid, False otherwise.
    """
    domain_name_pattern = r"^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$"
    return bool(re.match(domain_name_pattern, domain_name))

def convert_to_snake_case(input_string: str) -> str:
    """
    Convert a string to snake case.

    Args:
    input_string (str): The string to convert.

    Returns:
    str: The input string in snake case.
    """
    input_string = input_string.replace(" ", "_")
    input_string = re.sub(r"([A-Z])", r"_\1", input_string).lower()
    return input_string.lstrip("_")

def truncate_string(input_string: str, max_length: int = 50) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
    input_string (str): The string to truncate.
    max_length (int): The maximum length of the string. Defaults to 50.

    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[: max_length - 3] + "..."
    return input_string
```
