```python
"""
String utility module.

This module provides various functions for string manipulation and formatting.
"""

import re

def camel_case_to_snake_case(input_string: str) -> str:
    """
    Convert camel case string to snake case.

    Args:
        input_string (str): The camel case string to convert.

    Returns:
        str: The converted snake case string.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_string).lower()

def snake_case_to_camel_case(input_string: str) -> str:
    """
    Convert snake case string to camel case.

    Args:
        input_string (str): The snake case string to convert.

    Returns:
        str: The converted camel case string.
    """
    words = input_string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
        input_string (str): The string to truncate.
        max_length (int): The maximum length of the string.

    Returns:
        str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length - 3] + '...'
    return input_string

def indent_string(input_string: str, indent_level: int) -> str:
    """
    Indent a string by a specified number of spaces.

    Args:
        input_string (str): The string to indent.
        indent_level (int): The number of spaces to indent.

    Returns:
        str: The indented string.
    """
    indent = ' ' * indent_level
    return '\n'.join(indent + line for line in input_string.split('\n'))
```
