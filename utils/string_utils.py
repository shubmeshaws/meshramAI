```python
"""
String utility functions.
"""

def camel_to_snake_case(input_string: str) -> str:
    """
    Convert a camel case string to snake case.

    Args:
        input_string (str): The input string in camel case.

    Returns:
        str: The input string converted to snake case.
    """
    result = ""
    for char in input_string:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result


def snake_to_camel_case(input_string: str) -> str:
    """
    Convert a snake case string to camel case.

    Args:
        input_string (str): The input string in snake case.

    Returns:
        str: The input string converted to camel case.
    """
    components = input_string.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
        input_string (str): The input string.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The input string truncated to the specified maximum length.
    """
    if len(input_string) > max_length:
        return input_string[: max_length - 3] + "..."
    return input_string


def remove_special_chars(input_string: str) -> str:
    """
    Remove special characters from a string.

    Args:
        input_string (str): The input string.

    Returns:
        str: The input string with special characters removed.
    """
    return "".join(char for char in input_string if char.isalnum() or char.isspace())
```
