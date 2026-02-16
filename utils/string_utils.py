```python
"""
String utility functions for meshram project.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
    email (str): Email address to be validated.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def validate_ip_address(ip_address: str) -> bool:
    """
    Validate an IP address.

    Args:
    ip_address (str): IP address to be validated.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_regex, ip_address))

def camel_case_to_snake_case(input_string: str) -> str:
    """
    Convert a camel case string to snake case.

    Args:
    input_string (str): The string to be converted.

    Returns:
    str: The input string converted to snake case.
    """
    words = re.sub("([A-Z])", r"_\1", input_string).lower().strip()
    return words

def snake_case_to_camel_case(input_string: str) -> str:
    """
    Convert a snake case string to camel case.

    Args:
    input_string (str): The string to be converted.

    Returns:
    str: The input string converted to camel case.
    """
    words = input_string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to the specified length.

    Args:
    input_string (str): The string to be truncated.
    max_length (int): The maximum length of the output string.

    Returns:
    str: The input string truncated to the specified length.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string
```
