```python
"""
String utility functions.

This module provides useful string manipulation functions.
"""

def camel_to_snake(camel_str: str) -> str:
    """
    Convert a camelCase string to snake_case.

    Args:
    - camel_str (str): The input camelCase string.

    Returns:
    - str: The input string converted to snake_case.
    """
    snake_str = ""
    for i, char in enumerate(camel_str):
        if char.isupper() and i != 0:
            snake_str += "_" + char.lower()
        else:
            snake_str += char.lower()
    return snake_str


def snake_to_camel(snake_str: str) -> str:
    """
    Convert a snake_case string to camelCase.

    Args:
    - snake_str (str): The input snake_case string.

    Returns:
    - str: The input string converted to camelCase.
    """
    words = snake_str.split("_")
    camel_str = words[0].lower()
    for word in words[1:]:
        camel_str += word.capitalize()
    return camel_str


def remove_special_chars(input_str: str) -> str:
    """
    Remove special characters from a string.

    Args:
    - input_str (str): The input string.

    Returns:
    - str: The input string with special characters removed.
    """
    return "".join(char for char in input_str if char.isalnum() or char.isspace())


def truncate_string(input_str: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
    - input_str (str): The input string.
    - max_length (int): The maximum length of the output string.

    Returns:
    - str: The input string truncated to the specified maximum length.
    """
    if len(input_str) > max_length:
        return input_str[: max_length - 3] + "..."
    return input_str
```
