```python
"""
String utility functions.

This module contains functions for string manipulation and formatting.
"""

import re

def camel_case_to_snake_case(input_str):
    """
    Convert a camel case string to snake case.

    Args:
        input_str (str): The input string in camel case.

    Returns:
        str: The input string converted to snake case.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_str).lower()

def snake_case_to_camel_case(input_str):
    """
    Convert a snake case string to camel case.

    Args:
        input_str (str): The input string in snake case.

    Returns:
        str: The input string converted to camel case.
    """
    components = input_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

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
        return input_str[:max_length - 3] + '...'
    return input_str

def remove_special_chars(input_str):
    """
    Remove special characters from a string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The input string with special characters removed.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_str)

# Example usage:
if __name__ == '__main__':
    print(camel_case_to_snake_case('HelloWorld'))  # Output: hello_world
    print(snake_case_to_camel_case('hello_world'))  # Output: HelloWorld
    print(truncate_string('Very long string that needs to be truncated', 20))  # Output: Very long string...
    print(remove_special_chars('Hello, World!'))  # Output: Hello World
```
