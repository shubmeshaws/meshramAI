```python
"""
String utility functions.

This module provides various functions for string manipulation and formatting.
"""

import re

def camel_to_snake(name: str) -> str:
    """
    Convert a camelCase string to snake_case.

    Args:
    name (str): The input string in camelCase.

    Returns:
    str: The input string converted to snake_case.
    """
    name = re.sub('([A-Z])', r'_\1', name)
    return name.lower()

def snake_to_camel(name: str) -> str:
    """
    Convert a snake_case string to camelCase.

    Args:
    name (str): The input string in snake_case.

    Returns:
    str: The input string converted to camelCase.
    """
    components = name.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
    input_string (str): The input string to be truncated.
    max_length (int): The maximum length of the output string.

    Returns:
    str: The truncated string.
    """
    if len(input_string) <= max_length:
        return input_string
    else:
        return input_string[:max_length] + '...'

def remove_special_chars(input_string: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_string (str): The input string.

    Returns:
    str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)
```
