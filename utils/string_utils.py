```python
"""
This module provides utility functions for handling string operations.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if the input string is empty or contains only whitespace characters.

    Args:
    input_string (str): The input string to be checked.

    Returns:
    bool: True if the input string is empty, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validates if the input string is a valid email address.

    Args:
    email (str): The input string to be validated.

    Returns:
    bool: True if the input string is a valid email address, False otherwise.
    """
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(email_regex, email))

def remove_special_chars(input_string: str) -> str:
    """
    Removes special characters from the input string.

    Args:
    input_string (str): The input string to be cleaned.

    Returns:
    str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)

def camel_to_snake_case(input_string: str) -> str:
    """
    Converts a camel case string to snake case.

    Args:
    input_string (str): The input string to be converted.

    Returns:
    str: The input string in snake case.
    """
    return re.sub('([A-Z])', r'_\1', input_string).lower()

# Example usage
if __name__ == "__main__":
    print(is_empty_string("   "))  # True
    print(validate_email("example@example.com"))  # True
    print(remove_special_chars("Hello, World!"))  # HelloWorld
    print(camel_to_snake_case("HelloWorld"))  # hello_world
```
