```python
"""
String utility functions for text formatting and manipulation.
"""

import re

def camel_case_to_snake_case(input_str: str) -> str:
    """
    Convert a camel case string to snake case.

    Args:
    input_str (str): The input string in camel case.

    Returns:
    str: The input string converted to snake case.
    """
    return re.sub('([A-Z])', r'_\1', input_str).lower().lstrip('_')

def snake_case_to_camel_case(input_str: str) -> str:
    """
    Convert a snake case string to camel case.

    Args:
    input_str (str): The input string in snake case.

    Returns:
    str: The input string converted to camel case.
    """
    components = input_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def truncate_string(input_str: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
    input_str (str): The input string.
    max_length (int): The maximum allowed length.

    Returns:
    str: The input string truncated to the specified maximum length.
    """
    if len(input_str) > max_length:
        return input_str[:max_length - 3] + '...'
    return input_str

def remove_special_chars(input_str: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_str (str): The input string.

    Returns:
    str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9\s]+', '', input_str)
```
