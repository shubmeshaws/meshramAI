```python
"""
Utility functions for common string operations.
"""

import re

def trim_string(input_str, max_length=50):
    """
    Trim a string to a specified maximum length.

    Args:
        input_str (str): The input string to be trimmed.
        max_length (int): The maximum length of the output string. Defaults to 50.

    Returns:
        str: The trimmed string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + "..."
    return input_str

def remove_special_chars(input_str):
    """
    Remove special characters from a string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9\s]+', '', input_str)

def to_snake_case(input_str):
    """
    Convert a string to snake case.

    Args:
        input_str (str): The input string.

    Returns:
        str: The string in snake case.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_str).lower()

def to_title_case(input_str):
    """
    Convert a string to title case.

    Args:
        input_str (str): The input string.

    Returns:
        str: The string in title case.
    """
    return input_str.title()

def is_empty_string(input_str):
    """
    Check if a string is empty.

    Args:
        input_str (str): The input string.

    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return not input_str.strip()
```
