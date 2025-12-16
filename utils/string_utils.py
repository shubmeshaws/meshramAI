```python
"""
string_utils.py

A utility module containing functions for string manipulation and validation.
"""

import re

def is_empty(string: str) -> bool:
    """
    Checks if a string is empty or contains only whitespace.

    Args:
        string (str): The input string to check.

    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return not string.strip()

def validate_email(email: str) -> bool:
    """
    Validates an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def validate_ip_address(ip_address: str) -> bool:
    """
    Validates an IP address.

    Args:
        ip_address (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    ip_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return bool(re.match(ip_regex, ip_address))

def camel_case_to_snake_case(string: str) -> str:
    """
    Converts a camel case string to snake case.

    Args:
        string (str): The input string to convert.

    Returns:
        str: The converted string in snake case.
    """
    return re.sub(r"(?<!^)(?=[A-Z])", "_", string).lower()

def snake_case_to_camel_case(string: str) -> str:
    """
    Converts a snake case string to camel case.

    Args:
        string (str): The input string to convert.

    Returns:
        str: The converted string in camel case.
    """
    components = string.split("_")
    return components[0] + "".join(x.title() for x in components[1:])

# Example usage:
if __name__ == "__main__":
    print(is_empty("   "))  # Output: True
    print(validate_email("example@example.com"))  # Output: True
    print(validate_ip_address("192.168.1.1"))  # Output: True
    print(camel_case_to_snake_case("HelloWorld"))  # Output: hello_world
    print(snake_case_to_camel_case("hello_world"))  # Output: helloWorld
```
