```python
# utils/string_utils.py

"""
String utilities module.
"""

import re

def camel_case_to_snake_case(input_str: str) -> str:
    """
    Convert camel case string to snake case.

    Args:
        input_str (str): Input string in camel case.

    Returns:
        str: Converted string in snake case.
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def snake_case_to_camel_case(input_str: str) -> str:
    """
    Convert snake case string to camel case.

    Args:
        input_str (str): Input string in snake case.

    Returns:
        str: Converted string in camel case.
    """
    components = input_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def truncate_string(input_str: str, max_length: int = 50) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
        input_str (str): Input string.
        max_length (int): Maximum length of the output string. Defaults to 50.

    Returns:
        str: Truncated string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + '...'
    return input_str
```
