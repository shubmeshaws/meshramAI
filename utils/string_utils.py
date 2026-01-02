```python
"""
String utility functions.
"""

import re

def snake_to_camel(snake_str):
    """
    Convert a snake_case string to camelCase.

    Args:
        snake_str (str): The snake_case string.

    Returns:
        str: The camelCase string.
    """
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def camel_to_snake(camel_str):
    """
    Convert a camelCase string to snake_case.

    Args:
        camel_str (str): The camelCase string.

    Returns:
        str: The snake_case string.
    """
    snake_str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', snake_str).lower()

def remove_special_chars(input_str):
    """
    Remove special characters from a string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The string without special characters.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_str)

def truncate_string(input_str, max_length):
    """
    Truncate a string to a maximum length.

    Args:
        input_str (str): The input string.
        max_length (int): The maximum length.

    Returns:
        str: The truncated string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + '...'
    return input_str

# Example usage:
if __name__ == '__main__':
    print(snake_to_camel('hello_world'))  # Output: helloWorld
    print(camel_to_snake('helloWorld'))  # Output: hello_world
    print(remove_special_chars('Hello, World!'))  # Output: HelloWorld
    print(truncate_string('This is a very long string', 10))  # Output: This is a...
```
