```python
"""
String utility functions for the project.
"""

import re

def is_valid_ip_address(ip_address: str) -> bool:
    """
    Validate an IP address.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if re.match(pattern, ip_address):
        return all(0 <= int(part) <= 255 for part in ip_address.split("."))
    return False


def is_valid_domain_name(domain_name: str) -> bool:
    """
    Validate a domain name.

    Args:
    domain_name (str): The domain name to validate.

    Returns:
    bool: True if the domain name is valid, False otherwise.
    """
    pattern = r"^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$"
    return bool(re.match(pattern, domain_name, re.IGNORECASE))


def snake_to_camel_case(snake_str: str) -> str:
    """
    Convert a snake_case string to camelCase.

    Args:
    snake_str (str): The snake_case string to convert.

    Returns:
    str: The camelCase version of the input string.
    """
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def camel_to_snake_case(camel_str: str) -> str:
    """
    Convert a camelCase string to snake_case.

    Args:
    camel_str (str): The camelCase string to convert.

    Returns:
    str: The snake_case version of the input string.
    """
    snake_str = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", camel_str)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", snake_str).lower()
```
