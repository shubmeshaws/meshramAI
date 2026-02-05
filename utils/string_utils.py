```python
"""
Utility functions for string manipulation.
"""

import re

def camel_case_to_snake_case(input_str):
    """
    Converts a camel case string to snake case.
    
    Args:
    input_str (str): The input string in camel case.
    
    Returns:
    str: The input string converted to snake case.
    """
    # Use regular expression to find uppercase letters and insert an underscore before them
    snake_case_str = re.sub('([A-Z])', r'_\1', input_str).lower()
    # Remove leading underscore if present
    if snake_case_str.startswith('_'):
        snake_case_str = snake_case_str[1:]
    return snake_case_str


def snake_case_to_camel_case(input_str):
    """
    Converts a snake case string to camel case.
    
    Args:
    input_str (str): The input string in snake case.
    
    Returns:
    str: The input string converted to camel case.
    """
    # Split the string by underscores and capitalize each word
    camel_case_str = ''.join(word.capitalize() for word in input_str.split('_'))
    return camel_case_str


def remove_special_characters(input_str):
    """
    Removes special characters from a string.
    
    Args:
    input_str (str): The input string containing special characters.
    
    Returns:
    str: The input string with special characters removed.
    """
    # Use regular expression to replace non-alphanumeric characters with an empty string
    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str)
    return cleaned_str


def truncate_string(input_str, max_length):
    """
    Truncates a string to a specified maximum length.
    
    Args:
    input_str (str): The input string to be truncated.
    max_length (int): The maximum allowed length of the string.
    
    Returns:
    str: The input string truncated to the specified maximum length.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + '...'
    else:
        return input_str
```
