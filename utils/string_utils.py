```python
"""
This module provides utility functions for common string operations.
"""

import re

def remove_special_chars(input_str):
    """
    Removes special characters from the input string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The input string without special characters.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_str)

def convert_to_lowercase(input_str):
    """
    Converts the input string to lowercase.

    Args:
        input_str (str): The input string.

    Returns:
        str: The input string in lowercase.
    """
    return input_str.lower()

def remove_whitespace(input_str):
    """
    Removes leading and trailing whitespace from the input string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The input string without leading and trailing whitespace.
    """
    return input_str.strip()

def truncate_string(input_str, max_length):
    """
    Truncates the input string to the specified maximum length.

    Args:
        input_str (str): The input string.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The truncated input string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length]
    return input_str

def is_empty_string(input_str):
    """
    Checks if the input string is empty or contains only whitespace.

    Args:
        input_str (str): The input string.

    Returns:
        bool: True if the input string is empty or contains only whitespace, False otherwise.
    """
    return not input_str.strip()
```
