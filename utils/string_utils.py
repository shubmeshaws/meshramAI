```python
"""
String utility functions for manipulation and validation.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
    - email (str): The email address to validate.

    Returns:
    - bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def validate_ip_address(ip_address: str) -> bool:
    """
    Validate an IP address.

    Args:
    - ip_address (str): The IP address to validate.

    Returns:
    - bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return bool(re.match(ip_address_regex, ip_address))

def remove_special_characters(input_string: str) -> str:
    """
    Remove special characters from a string.

    Args:
    - input_string (str): The string to remove special characters from.

    Returns:
    - str: The string with special characters removed.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

def slugify(input_string: str) -> str:
    """
    Convert a string to a slug.

    Args:
    - input_string (str): The string to convert to a slug.

    Returns:
    - str: The string converted to a slug.
    """
    return re.sub(r'[^a-zA-Z0-9\s-]', '', input_string).lower().replace(' ', '-')

# Example usage:
if __name__ == "__main__":
    print(validate_email("example@example.com"))  # Output: True
    print(validate_ip_address("192.168.1.1"))  # Output: True
    print(remove_special_characters("Hello, World!"))  # Output: "Hello World"
    print(slugify("Hello World"))  # Output: "hello-world"
```
