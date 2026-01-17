```python
"""
String Utilities Module
========================
This module contains functions for common string operations.
"""

import re

def camel_case_to_snake_case(input_string: str) -> str:
    """
    Convert a camel case string to snake case.
    
    Args:
        input_string (str): The string to convert.
    
    Returns:
        str: The converted string.
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def snake_case_to_camel_case(input_string: str) -> str:
    """
    Convert a snake case string to camel case.
    
    Args:
        input_string (str): The string to convert.
    
    Returns:
        str: The converted string.
    """
    words = input_string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

def remove_special_characters(input_string: str) -> str:
    """
    Remove all special characters from a string.
    
    Args:
        input_string (str): The string to clean.
    
    Returns:
        str: The cleaned string.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)

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
        return input_string[:max_length] + '...'
    else:
        return input_string
```
