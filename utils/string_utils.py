```python
# utils/string_utils.py

"""
Utility module for string manipulation and formatting.
"""

import re

def camel_to_snake_case(input_str):
    """
    Convert a camel case string to snake case.

    Args:
        input_str (str): The input string in camel case.

    Returns:
        str: The input string converted to snake case.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_str).lower()

def snake_to_camel_case(input_str):
    """
    Convert a snake case string to camel case.

    Args:
        input_str (str): The input string in snake case.

    Returns:
        str: The input string converted to camel case.
    """
    components = input_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

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

def remove_special_chars(input_str):
    """
    Remove special characters from a string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The input string with special characters removed.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_str)
```
