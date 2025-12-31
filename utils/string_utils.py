```python
"""
String utility functions.

This module provides various functions for string manipulation and processing.
"""

import re

def is_empty(string: str) -> bool:
    """
    Check if a string is empty.

    Args:
    string (str): The input string.

    Returns:
    bool: True if the string is empty, False otherwise.
    """
    return not string.strip()

def is_match(pattern: str, string: str) -> bool:
    """
    Check if a string matches a regular expression pattern.

    Args:
    pattern (str): The regular expression pattern.
    string (str): The input string.

    Returns:
    bool: True if the string matches the pattern, False otherwise.
    """
    return bool(re.match(pattern, string))

def remove_special_chars(string: str) -> str:
    """
    Remove special characters from a string.

    Args:
    string (str): The input string.

    Returns:
    str: The string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', string)

def truncate_string(string: str, max_length: int) -> str:
    """
    Truncate a string to a specified length.

    Args:
    string (str): The input string.
    max_length (int): The maximum length of the string.

    Returns:
    str: The truncated string.
    """
    if len(string) > max_length:
        return string[:max_length] + '...'
    return string

def to_title_case(string: str) -> str:
    """
    Convert a string to title case.

    Args:
    string (str): The input string.

    Returns:
    str: The string in title case.
    """
    return string.title()

def to_snake_case(string: str) -> str:
    """
    Convert a string to snake case.

    Args:
    string (str): The input string.

    Returns:
    str: The string in snake case.
    """
    return re.sub(' ', '_', string).lower()
```
