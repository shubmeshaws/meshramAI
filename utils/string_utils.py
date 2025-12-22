```python
"""
String utility functions.
"""

import re

def camel_case_to_snake_case(input_str):
    """
    Converts a camel case string to snake case.

    Args:
        input_str (str): The input string in camel case.

    Returns:
        str: The input string in snake case.
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def snake_case_to_camel_case(input_str):
    """
    Converts a snake case string to camel case.

    Args:
        input_str (str): The input string in snake case.

    Returns:
        str: The input string in camel case.
    """
    components = input_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def remove_special_chars(input_str):
    """
    Removes special characters from a string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The input string without special characters.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_str)

def truncate_string(input_str, max_length):
    """
    Truncates a string to a specified maximum length.

    Args:
        input_str (str): The input string.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The input string truncated to the specified maximum length.
    """
    if len(input_str) <= max_length:
        return input_str
    else:
        return input_str[:max_length - 3] + '...'

# Example usage:
if __name__ == "__main__":
    print(camel_case_to_snake_case("HelloWorld"))  # hello_world
    print(snake_case_to_camel_case("hello_world"))  # HelloWorld
    print(remove_special_chars("Hello, World!"))  # HelloWorld
    print(truncate_string("Hello, World! This is a test string.", 20))  # Hello, World! This...
```
