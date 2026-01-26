```python
"""
This module provides a set of utility functions for common string operations.
"""

import re

def camel_case_to_snake_case(camel_case_str):
    """
    Convert a camel case string to snake case.

    Args:
        camel_case_str (str): The input camel case string.

    Returns:
        str: The input string converted to snake case.
    """
    snake_case_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_str).lower()
    return snake_case_str


def snake_case_to_camel_case(snake_case_str):
    """
    Convert a snake case string to camel case.

    Args:
        snake_case_str (str): The input snake case string.

    Returns:
        str: The input string converted to camel case.
    """
    words = snake_case_str.split('_')
    camel_case_str = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case_str


def remove_special_chars(input_str):
    """
    Remove special characters from a string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The input string with special characters removed.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_str)


def truncate_string(input_str, max_length):
    """
    Truncate a string to a specified maximum length.

    Args:
        input_str (str): The input string.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The input string truncated to the specified maximum length.
    """
    if len(input_str) > max_length:
        return input_str[:max_length - 3] + '...'
    return input_str
```
