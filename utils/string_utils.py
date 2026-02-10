```python
"""
Utility module for common string operations.
"""

import re

def camel_case_to_snake_case(s):
    """
    Convert a camelCase string to snake_case.
    
    Args:
        s (str): The input string.
    
    Returns:
        str: The input string converted to snake_case.
    """
    s = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
    return s

def snake_case_to_camel_case(s):
    """
    Convert a snake_case string to camelCase.
    
    Args:
        s (str): The input string.
    
    Returns:
        str: The input string converted to camelCase.
    """
    components = s.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def strip_whitespace(s):
    """
    Remove leading and trailing whitespace from a string.
    
    Args:
        s (str): The input string.
    
    Returns:
        str: The input string with leading and trailing whitespace removed.
    """
    return s.strip()

def truncate_string(s, max_length):
    """
    Truncate a string to a specified maximum length.
    
    Args:
        s (str): The input string.
        max_length (int): The maximum length of the output string.
    
    Returns:
        str: The input string truncated to the specified maximum length.
    """
    if len(s) > max_length:
        return s[:max_length] + '...'
    return s
```
