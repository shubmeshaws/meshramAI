```python
"""
String Utilities Module
=======================

This module provides various string manipulation functions.
"""

import re

def camel_to_snake_case(input_str):
    """
    Convert camel case string to snake case.

    Args:
        input_str (str): Input string in camel case.

    Returns:
        str: Input string converted to snake case.
    """
    return re.sub('([A-Z])', r'_\1', input_str).lower().lstrip('_')

def snake_to_camel_case(input_str):
    """
    Convert snake case string to camel case.

    Args:
        input_str (str): Input string in snake case.

    Returns:
        str: Input string converted to camel case.
    """
    words = input_str.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

def truncate_string(input_str, max_length):
    """
    Truncate a string to a specified maximum length.

    Args:
        input_str (str): Input string to be truncated.
        max_length (int): Maximum allowed length.

    Returns:
        str: Truncated input string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length - 3] + '...'
    return input_str

def remove_special_chars(input_str):
    """
    Remove special characters from a string.

    Args:
        input_str (str): Input string containing special characters.

    Returns:
        str: Input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_str)

# Example usage
if __name__ == "__main__":
    print(camel_to_snake_case("HelloWorld"))  # Output: hello_world
    print(snake_to_camel_case("hello_world"))  # Output: HelloWorld
    print(truncate_string("This is a very long string", 20))  # Output: This is a very ...
    print(remove_special_chars("Hello, World!"))  # Output: HelloWorld
```
