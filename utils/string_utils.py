```python
"""
Utility module for common string operations.
"""

import re

def camel_to_snake_case(input_string: str) -> str:
    """
    Converts a camel case string to snake case.

    Args:
    input_string (str): The input string in camel case.

    Returns:
    str: The input string in snake case.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_string).lower()

def snake_to_camel_case(input_string: str) -> str:
    """
    Converts a snake case string to camel case.

    Args:
    input_string (str): The input string in snake case.

    Returns:
    str: The input string in camel case.
    """
    components = input_string.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates a string to a specified maximum length.

    Args:
    input_string (str): The input string.
    max_length (int): The maximum allowed length.

    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + '...'
    return input_string

def remove_special_characters(input_string: str) -> str:
    """
    Removes special characters from a string.

    Args:
    input_string (str): The input string.

    Returns:
    str: The string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)
```
