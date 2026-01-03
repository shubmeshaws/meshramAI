```python
"""
String utility functions.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if a string is empty or None.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the string is empty or None, False otherwise.
    """
    return input_string is None or len(input_string.strip()) == 0


def validate_email(email: str) -> bool:
    """
    Validates an email address using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))


def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates a string to a specified maximum length.

    Args:
        input_string (str): The input string to truncate.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[: max_length - 3] + "..."
    return input_string


def snake_case_to_camel_case(snake_case_string: str) -> str:
    """
    Converts a snake_case string to camelCase.

    Args:
        snake_case_string (str): The input string in snake_case.

    Returns:
        str: The input string converted to camelCase.
    """
    components = snake_case_string.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def camel_case_to_snake_case(camel_case_string: str) -> str:
    """
    Converts a camelCase string to snake_case.

    Args:
        camel_case_string (str): The input string in camelCase.

    Returns:
        str: The input string converted to snake_case.
    """
    snake_case_string = ""
    for char in camel_case_string:
        if char.isupper():
            snake_case_string += "_" + char.lower()
        else:
            snake_case_string += char
    return snake_case_string
```
