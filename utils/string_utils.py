```python
"""
Utility functions for string manipulation and formatting.
"""

import re

def camel_case_to_snake_case(input_str):
    """
    Convert a camelCase string to snake_case.
    
    Args:
        input_str (str): The input string in camelCase.
    
    Returns:
        str: The input string converted to snake_case.
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def snake_case_to_camel_case(input_str):
    """
    Convert a snake_case string to camelCase.
    
    Args:
        input_str (str): The input string in snake_case.
    
    Returns:
        str: The input string converted to camelCase.
    """
    components = input_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def truncate_string(input_str, max_length):
    """
    Truncate a string to a specified maximum length.
    
    Args:
        input_str (str): The input string to be truncated.
        max_length (int): The maximum length of the output string.
    
    Returns:
        str: The input string truncated to the specified maximum length.
    """
    if len(input_str) > max_length:
        return input_str[:max_length - 3] + '...'
    else:
        return input_str

def remove_special_chars(input_str):
    """
    Remove special characters from a string.
    
    Args:
        input_str (str): The input string.
    
    Returns:
        str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_str)
```
