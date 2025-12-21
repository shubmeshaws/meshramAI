```python
"""
String utility module.

This module provides functions for string manipulation and validation.
"""

import re

def is_valid_ip(ip_address: str) -> bool:
    """
    Validate an IP address.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_pattern, ip_address))

def is_valid_uuid(uuid_to_test: str) -> bool:
    """
    Validate a UUID.

    Args:
    uuid_to_test (str): The UUID to validate.

    Returns:
    bool: True if the UUID is valid, False otherwise.
    """
    regex = re.compile(r'^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}$', re.I)
    match = regex.match(uuid_to_test)
    return bool(match)

def camel_case_to_snake_case(name: str) -> str:
    """
    Convert a camel case string to snake case.

    Args:
    name (str): The string to convert.

    Returns:
    str: The snake case string.
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def snake_case_to_camel_case(name: str) -> str:
    """
    Convert a snake case string to camel case.

    Args:
    name (str): The string to convert.

    Returns:
    str: The camel case string.
    """
    components = name.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
```
