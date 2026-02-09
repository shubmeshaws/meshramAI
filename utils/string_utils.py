```python
"""
String utility functions.
"""

import re

def snake_to_camel_case(input_str):
    """
    Convert a snake_case string to camelCase.

    Args:
        input_str (str): The input string in snake_case.

    Returns:
        str: The input string converted to camelCase.
    """
    words = input_str.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])

def camel_to_snake_case(input_str):
    """
    Convert a camelCase string to snake_case.

    Args:
        input_str (str): The input string in camelCase.

    Returns:
        str: The input string converted to snake_case.
    """
    return re.sub(r"([A-Z])", r"_\1", input_str).lower()

def remove_special_chars(input_str):
    """
    Remove special characters from a string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The input string with special characters removed.
    """
    return re.sub(r"[^a-zA-Z0-9\s]", "", input_str)

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
        return input_str[:max_length - 3] + "..."
    return input_str

# Example usage:
if __name__ == "__main__":
    print(snake_to_camel_case("hello_world"))  # Output: helloWorld
    print(camel_to_snake_case("helloWorld"))  # Output: hello_world
    print(remove_special_chars("Hello, World!"))  # Output: Hello World
    print(truncate_string("This is a very long string", 20))  # Output: This is a very long...
```
