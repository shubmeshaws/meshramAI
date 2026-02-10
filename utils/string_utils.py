```python
"""
String utility functions for validation and manipulation.
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

def remove_special_characters(input_string: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_string (str): The string to remove special characters from.

    Returns:
    str: The string without special characters.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a specified length.

    Args:
    input_string (str): The string to truncate.
    max_length (int): The maximum length of the string.

    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    else:
        return input_string

# Example usage:
if __name__ == "__main__":
    print(validate_email("test@example.com"))  # True
    print(validate_ip_address("192.168.1.1"))  # True
    print(remove_special_characters("Hello, World!"))  # HelloWorld
    print(truncate_string("This is a very long string", 10))  # This is a...
```
