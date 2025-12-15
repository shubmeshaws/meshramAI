```python
"""
Utility functions for string manipulation and formatting.
"""

import re

def camel_case_to_snake_case(input_string):
    """
    Convert a camel case string to snake case.

    Args:
        input_string (str): The input string in camel case.

    Returns:
        str: The input string converted to snake case.
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def snake_case_to_camel_case(input_string):
    """
    Convert a snake case string to camel case.

    Args:
        input_string (str): The input string in snake case.

    Returns:
        str: The input string converted to camel case.
    """
    words = input_string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

def truncate_string(input_string, max_length):
    """
    Truncate a string to a specified maximum length.

    Args:
        input_string (str): The input string.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The input string truncated to the specified maximum length.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + '...'
    return input_string

def remove_whitespace(input_string):
    """
    Remove all whitespace characters from a string.

    Args:
        input_string (str): The input string.

    Returns:
        str: The input string with all whitespace characters removed.
    """
    return input_string.replace(' ', '')
```
