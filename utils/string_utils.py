```python
"""
String utilities module.

This module provides a set of functions for string operations, including validation, manipulation, and formatting.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Check if a string is empty or contains only whitespace.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the string is empty or contains only whitespace, False otherwise.
    """
    return not input_string.strip()

def validate_email(input_string: str) -> bool:
    """
    Validate an email address.

    Args:
        input_string (str): The input string to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, input_string))

def remove_special_chars(input_string: str) -> str:
    """
    Remove special characters from a string.

    Args:
        input_string (str): The input string to process.

    Returns:
        str: The input string with special characters removed.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

def format_string(input_string: str, **kwargs) -> str:
    """
    Format a string using keyword arguments.

    Args:
        input_string (str): The input string to format.
        **kwargs: Keyword arguments to use for formatting.

    Returns:
        str: The formatted string.
    """
    return input_string.format(**kwargs)

def camel_case_to_snake_case(input_string: str) -> str:
    """
    Convert a camel case string to snake case.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: The input string in snake case.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_string).lower()

# Example usage
if __name__ == "__main__":
    print(is_empty_string(""))  # True
    print(validate_email("example@example.com"))  # True
    print(remove_special_chars("Hello, World!"))  # "Hello World"
    print(format_string("Hello, {}!", name="World"))  # "Hello, World!"
    print(camel_case_to_snake_case("HelloWorld"))  # "hello_world"
```
