```python
"""
String utility module.

This module provides functions for string manipulation, including text formatting and validation.
"""

import re

def camel_case_to_snake_case(input_str):
    """
    Convert a camel case string to snake case.

    Args:
        input_str (str): The input string in camel case.

    Returns:
        str: The input string in snake case.
    """
    return re.sub('(?<!^)(?=[A-Z])', '_', input_str).lower()

def snake_case_to_camel_case(input_str):
    """
    Convert a snake case string to camel case.

    Args:
        input_str (str): The input string in snake case.

    Returns:
        str: The input string in camel case.
    """
    components = input_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def validate_email(input_str):
    """
    Validate an email address.

    Args:
        input_str (str): The input string to validate.

    Returns:
        bool: True if the input string is a valid email address, False otherwise.
    """
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(email_regex, input_str))

def truncate_string(input_str, max_length):
    """
    Truncate a string to a specified maximum length.

    Args:
        input_str (str): The input string to truncate.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The truncated input string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + '...'
    return input_str
```
