```python
"""
String Utilities Module
=======================

This module provides various utility functions for string operations.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if the input string is empty or contains only whitespace characters.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the input string is empty or contains only whitespace characters, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validates an email address using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def remove_special_characters(input_string: str) -> str:
    """
    Removes special characters from the input string.

    Args:
        input_string (str): The input string to clean.

    Returns:
        str: The input string with special characters removed.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

def format_string(input_string: str, **kwargs) -> str:
    """
    Formats the input string using the provided keyword arguments.

    Args:
        input_string (str): The input string to format.
        **kwargs: Keyword arguments to use for formatting.

    Returns:
        str: The formatted input string.
    """
    return input_string.format(**kwargs)

# Example usage:
if __name__ == "__main__":
    print(is_empty_string(""))  # Output: True
    print(validate_email("test@example.com"))  # Output: True
    print(remove_special_characters("Hello, World!"))  # Output: "Hello World"
    print(format_string("Hello, {name}!", name="John"))  # Output: "Hello, John!"
```
