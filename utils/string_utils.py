```python
"""
String utility functions for validation and manipulation.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate an email address.
    
    Args:
    email (str): The email address to be validated.
    
    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def validate_ip_address(ip_address: str) -> bool:
    """
    Validate an IP address.
    
    Args:
    ip_address (str): The IP address to be validated.
    
    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_regex, ip_address))

def camel_case_to_snake_case(camel_case_string: str) -> str:
    """
    Convert a camel case string to snake case.
    
    Args:
    camel_case_string (str): The camel case string to be converted.
    
    Returns:
    str: The snake case equivalent of the input string.
    """
    snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()
    return snake_case_string

def snake_case_to_camel_case(snake_case_string: str) -> str:
    """
    Convert a snake case string to camel case.
    
    Args:
    snake_case_string (str): The snake case string to be converted.
    
    Returns:
    str: The camel case equivalent of the input string.
    """
    components = snake_case_string.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# Example usage
if __name__ == "__main__":
    print(validate_email("test@example.com"))  # True
    print(validate_ip_address("192.168.1.1"))  # True
    print(camel_case_to_snake_case("HelloWorld"))  # hello_world
    print(snake_case_to_camel_case("hello_world"))  # helloWorld
```
