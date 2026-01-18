```python
"""
String utility functions.

This module provides functions for string manipulation and formatting.
"""

import re

def snake_to_camel_case(snake_str):
    """
    Convert a snake case string to camel case.

    Args:
        snake_str (str): The input string in snake case.

    Returns:
        str: The input string converted to camel case.
    """
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def camel_to_snake_case(camel_str):
    """
    Convert a camel case string to snake case.

    Args:
        camel_str (str): The input string in camel case.

    Returns:
        str: The input string converted to snake case.
    """
    snake_str = re.sub('([A-Z])', r'_\1', camel_str).lower()
    return snake_str.lstrip('_')

def remove_whitespace(input_str):
    """
    Remove all whitespace characters from a string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The input string with all whitespace characters removed.
    """
    return input_str.replace(' ', '')

def truncate_string(input_str, max_length):
    """
    Truncate a string to a specified maximum length.

    Args:
        input_str (str): The input string.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The input string truncated to the specified maximum length.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + '...'
    return input_str

# Example usage:
if __name__ == '__main__':
    print(snake_to_camel_case('hello_world'))  # Output: helloWorld
    print(camel_to_snake_case('helloWorld'))  # Output: hello_world
    print(remove_whitespace('hello world'))  # Output: helloworld
    print(truncate_string('hello world, this is a long string', 15))  # Output: hello world, th...
```
