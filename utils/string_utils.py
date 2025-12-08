```python
# utils/string_utils.py

import re

def is_valid_ipv4(ip_address: str) -> bool:
    """
    Validate an IPv4 address.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(pattern, ip_address))

def is_valid_ipv6(ip_address: str) -> bool:
    """
    Validate an IPv6 address.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    pattern = r"^([a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}$"
    return bool(re.match(pattern, ip_address))

def remove_empty_lines(text: str) -> str:
    """
    Remove empty lines from a given text.

    Args:
    text (str): The text to remove empty lines from.

    Returns:
    str: The text with empty lines removed.
    """
    return "\n".join([line for line in text.split("\n") if line.strip()])

def truncate_string(text: str, max_length: int) -> str:
    """
    Truncate a string to a maximum length.

    Args:
    text (str): The text to truncate.
    max_length (int): The maximum length of the text.

    Returns:
    str: The truncated text.
    """
    if len(text) > max_length:
        return text[:max_length - 3] + "..."
    return text

def indent_text(text: str, indent: int) -> str:
    """
    Indent a given text by a specified number of spaces.

    Args:
    text (str): The text to indent.
    indent (int): The number of spaces to indent.

    Returns:
    str: The indented text.
    """
    return "\n".join([" " * indent + line for line in text.split("\n")])
```
