```python
"""
Utility functions for string manipulation.
"""

import re

def to_title_case(input_string: str) -> str:
    """
    Converts a string to title case.
    
    Args:
    input_string (str): The string to convert.
    
    Returns:
    str: The input string in title case.
    """
    return input_string.title()

def remove_special_chars(input_string: str) -> str:
    """
    Removes special characters from a string.
    
    Args:
    input_string (str): The string to clean.
    
    Returns:
    str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9\s]+', '', input_string)

def remove_extra_spaces(input_string: str) -> str:
    """
    Removes extra spaces from a string.
    
    Args:
    input_string (str): The string to clean.
    
    Returns:
    str: The input string with extra spaces removed.
    """
    return re.sub(' +', ' ', input_string)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates a string to a specified length.
    
    Args:
    input_string (str): The string to truncate.
    max_length (int): The maximum length of the string.
    
    Returns:
    str: The input string truncated to the specified length.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + '...'
    return input_string
```
