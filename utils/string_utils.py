```python
"""
String utility module.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
    email (str): Email address to validate.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def validate_ip_address(ip_address: str) -> bool:
    """
    Validate an IP address.

    Args:
    ip_address (str): IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_regex, ip_address))

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
    input_string (str): Input string to truncate.
    max_length (int): Maximum length of the output string.

    Returns:
    str: Truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length - 3] + "..."
    return input_string

def remove_special_characters(input_string: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_string (str): Input string to process.

    Returns:
    str: String with special characters removed.
    """
    return re.sub(r"[^a-zA-Z0-9\s]", "", input_string)

def to_snake_case(input_string: str) -> str:
    """
    Convert a string to snake case.

    Args:
    input_string (str): Input string to convert.

    Returns:
    str: String in snake case.
    """
    return re.sub(r"([A-Z])", r"_\1", input_string).lower().lstrip("_")
```
