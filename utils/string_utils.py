```python
"""
Utility functions for handling string operations.

This module provides functions for string validation, formatting, and manipulation.
It can be used throughout the project to ensure consistent string handling.

Examples:
    >>> from utils.string_utils import is_empty, trim, to_lower
    >>> is_empty("")
    True
    >>> trim("   hello world   ")
    'hello world'
    >>> to_lower("HELLO WORLD")
    'hello world'
"""

def is_empty(s: str) -> bool:
    """
    Checks if a string is empty or contains only whitespace characters.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is empty or contains only whitespace characters, False otherwise.
    """
    return not s.strip()


def trim(s: str) -> str:
    """
    Removes leading and trailing whitespace characters from a string.

    Args:
        s (str): The input string to trim.

    Returns:
        str: The trimmed string.
    """
    return s.strip()


def to_lower(s: str) -> str:
    """
    Converts a string to lowercase.

    Args:
        s (str): The input string to convert.

    Returns:
        str: The converted string in lowercase.
    """
    return s.lower()


def to_upper(s: str) -> str:
    """
    Converts a string to uppercase.

    Args:
        s (str): The input string to convert.

    Returns:
        str: The converted string in uppercase.
    """
    return s.upper()


def is_valid_identifier(s: str) -> bool:
    """
    Checks if a string is a valid identifier (contains only letters, digits, and underscores).

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a valid identifier, False otherwise.
    """
    return s.isidentifier()


def format_string(template: str, **kwargs) -> str:
    """
    Formats a string using keyword arguments.

    Args:
        template (str): The input string template to format.
        **kwargs: Keyword arguments to replace in the template.

    Returns:
        str: The formatted string.
    """
    return template.format(**kwargs)


# Example usage:
if __name__ == "__main__":
    print(is_empty(""))  # Output: True
    print(trim("   hello world   "))  # Output: 'hello world'
    print(to_lower("HELLO WORLD"))  # Output: 'hello world'
    print(is_valid_identifier("hello_world"))  # Output: True
    print(format_string("Hello, {}!", name="John"))  # Output: 'Hello, John!'
```
