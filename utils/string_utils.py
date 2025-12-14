```python
# utils/string_utils.py

"""
Utility functions for common string operations.
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
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def validate_ip_address(ip_address: str) -> bool:
    """
    Validate an IP address.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return bool(re.match(ip_address_regex, ip_address))

def format_string(input_string: str, **kwargs) -> str:
    """
    Format a string using keyword arguments.

    Args:
    input_string (str): The string to format.
    **kwargs: Keyword arguments to replace placeholders in the string.

    Returns:
    str: The formatted string.
    """
    return input_string.format(**kwargs)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a maximum length.

    Args:
    input_string (str): The string to truncate.
    max_length (int): The maximum length of the string.

    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length - 3] + "..."
    return input_string

# Example usage
if __name__ == "__main__":
    print(validate_email("example@example.com"))  # True
    print(validate_ip_address("192.168.1.1"))  # True
    print(format_string("Hello, {name}!", name="John"))  # Hello, John!
    print(truncate_string("This is a very long string", 10))  # This is a...
```
