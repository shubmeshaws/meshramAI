```python
"""
String utility module for common string operations.

This module provides functions for validating, formatting, and manipulating strings.
"""

import re

def is_empty(string: str) -> bool:
    """
    Check if a string is empty or contains only whitespace characters.

    Args:
        string (str): The input string to check.

    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return not string.strip()

def validate_email(email: str) -> bool:
    """
    Validate an email address using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def truncate_string(string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
        string (str): The input string to truncate.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The truncated string.
    """
    if len(string) > max_length:
        return string[:max_length] + "..."
    return string

def snake_case_to_camel_case(string: str) -> str:
    """
    Convert a snake_case string to camelCase.

    Args:
        string (str): The input string to convert.

    Returns:
        str: The converted string.
    """
    components = string.split("_")
    return components[0] + "".join(x.title() for x in components[1:])

# Example usage
if __name__ == "__main__":
    print(is_empty("   "))  # True
    print(validate_email("example@example.com"))  # True
    print(truncate_string("This is a very long string", 10))  # "This is a..."
    print(snake_case_to_camel_case("hello_world"))  # "helloWorld"
```
