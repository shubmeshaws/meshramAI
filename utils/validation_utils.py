```python
"""
Validation utility file for various data types.
"""

import re
from typing import List, Dict, Any

def validate_string(input_string: str, min_length: int = 1, max_length: int = 100) -> bool:
    """
    Validate a string based on its length.

    Args:
    input_string (str): The string to be validated.
    min_length (int): The minimum allowed length. Defaults to 1.
    max_length (int): The maximum allowed length. Defaults to 100.

    Returns:
    bool: True if the string is valid, False otherwise.
    """
    return min_length <= len(input_string) <= max_length


def validate_integer(input_integer: int, min_value: int = 0, max_value: int = 100) -> bool:
    """
    Validate an integer based on its value.

    Args:
    input_integer (int): The integer to be validated.
    min_value (int): The minimum allowed value. Defaults to 0.
    max_value (int): The maximum allowed value. Defaults to 100.

    Returns:
    bool: True if the integer is valid, False otherwise.
    """
    return min_value <= input_integer <= max_value


def validate_list(input_list: List[Any], min_length: int = 1, max_length: int = 100) -> bool:
    """
    Validate a list based on its length.

    Args:
    input_list (List[Any]): The list to be validated.
    min_length (int): The minimum allowed length. Defaults to 1.
    max_length (int): The maximum allowed length. Defaults to 100.

    Returns:
    bool: True if the list is valid, False otherwise.
    """
    return min_length <= len(input_list) <= max_length


def validate_email(input_email: str) -> bool:
    """
    Validate an email address using a regular expression.

    Args:
    input_email (str): The email address to be validated.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, input_email))


def validate_dict(input_dict: Dict[str, Any], required_keys: List[str]) -> bool:
    """
    Validate a dictionary based on the presence of required keys.

    Args:
    input_dict (Dict[str, Any]): The dictionary to be validated.
    required_keys (List[str]): The list of required keys.

    Returns:
    bool: True if the dictionary is valid, False otherwise.
    """
    return all(key in input_dict for key in required_keys)
```
