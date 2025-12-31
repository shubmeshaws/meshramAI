```python
"""
This module provides utility functions for common string operations.
"""

def camel_to_snake_case(input_string: str) -> str:
    """
    Converts a camel case string to snake case.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: The input string in snake case.
    """
    snake_case = ""
    for i, char in enumerate(input_string):
        if char.isupper():
            if i > 0:
                snake_case += "_"
            snake_case += char.lower()
        else:
            snake_case += char
    return snake_case


def snake_to_camel_case(input_string: str) -> str:
    """
    Converts a snake case string to camel case.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: The input string in camel case.
    """
    words = input_string.split("_")
    camel_case = words[0]
    for word in words[1:]:
        camel_case += word.capitalize()
    return camel_case


def remove_special_chars(input_string: str) -> str:
    """
    Removes special characters from a string.

    Args:
        input_string (str): The input string to remove special characters from.

    Returns:
        str: The input string with special characters removed.
    """
    return "".join(char for char in input_string if char.isalnum() or char.isspace())


def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates a string to a specified maximum length.

    Args:
        input_string (str): The input string to truncate.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The input string truncated to the specified maximum length.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    else:
        return input_string
```
