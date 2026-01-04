```python
"""
String utility functions for data manipulation.
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
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def remove_special_chars(input_str: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_str (str): The input string.

    Returns:
    str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_str)


def truncate_string(input_str: str, max_length: int) -> str:
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


def is_empty_string(input_str: str) -> bool:
    """
    Check if a string is empty or contains only whitespace.

    Args:
    input_str (str): The input string.

    Returns:
    bool: True if the input string is empty or contains only whitespace, False otherwise.
    """
    return input_str.strip() == ''
```
