```python
"""
String Utilities Module
========================
This module contains functions for common string operations.
"""

import re

def camel_to_snake_case(input_string):
    """
    Converts a camel case string to snake case.

    Args:
        input_string (str): The input string in camel case.

    Returns:
        str: The input string converted to snake case.
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def snake_to_camel_case(input_string):
    """
    Converts a snake case string to camel case.

    Args:
        input_string (str): The input string in snake case.

    Returns:
        str: The input string converted to camel case.
    """
    components = input_string.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def truncate_string(input_string, max_length):
    """
    Truncates a string to a specified maximum length.

    Args:
        input_string (str): The input string.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The input string truncated to the specified maximum length.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + '...'
    return input_string

def remove_special_characters(input_string):
    """
    Removes special characters from a string.

    Args:
        input_string (str): The input string.

    Returns:
        str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)
```
