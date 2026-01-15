```python
"""
String utility functions.
"""

import re

def snake_case_to_camel_case(snake_case_string: str) -> str:
    """
    Converts a snake_case string to camelCase.

    Args:
    snake_case_string (str): The string to convert.

    Returns:
    str: The camelCase version of the input string.
    """
    components = snake_case_string.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def camel_case_to_snake_case(camel_case_string: str) -> str:
    """
    Converts a camelCase string to snake_case.

    Args:
    camel_case_string (str): The string to convert.

    Returns:
    str: The snake_case version of the input string.
    """
    snake_case_string = re.sub('([A-Z])', r'_\1', camel_case_string).lower()
    return snake_case_string.lstrip('_')


def remove_special_characters(input_string: str) -> str:
    """
    Removes special characters from a string.

    Args:
    input_string (str): The string to clean.

    Returns:
    str: The cleaned string.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)


def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates a string to a specified length.

    Args:
    input_string (str): The string to truncate.
    max_length (int): The maximum length of the output string.

    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + '...'
    else:
        return input_string
```
