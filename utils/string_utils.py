```python
"""
String utility module.

This module provides functions for string manipulation and formatting.
"""

import re

def camel_to_snake_case(camel_str: str) -> str:
    """
    Convert a camel case string to snake case.

    Args:
    - camel_str (str): The camel case string to convert.

    Returns:
    - str: The snake case equivalent of the input string.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()


def snake_to_camel_case(snake_str: str) -> str:
    """
    Convert a snake case string to camel case.

    Args:
    - snake_str (str): The snake case string to convert.

    Returns:
    - str: The camel case equivalent of the input string.
    """
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def truncate_string(input_str: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
    - input_str (str): The input string to truncate.
    - max_length (int): The maximum length of the output string.

    Returns:
    - str: The truncated string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length - 3] + '...'
    return input_str


def pad_string(input_str: str, min_length: int, pad_char: str = ' ') -> str:
    """
    Pad a string to a specified minimum length.

    Args:
    - input_str (str): The input string to pad.
    - min_length (int): The minimum length of the output string.
    - pad_char (str): The character to use for padding (default: space).

    Returns:
    - str: The padded string.
    """
    if len(input_str) < min_length:
        return input_str + pad_char * (min_length - len(input_str))
    return input_str
```
