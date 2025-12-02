```python
"""
Validation utility functions.
"""

import re

def validate_string(input_string, min_length=1, max_length=255, allow_empty=False):
    """
    Validate a string.

    Args:
        input_string (str): The input string to validate.
        min_length (int, optional): The minimum length of the string. Defaults to 1.
        max_length (int, optional): The maximum length of the string. Defaults to 255.
        allow_empty (bool, optional): Whether to allow empty strings. Defaults to False.

    Returns:
        bool: True if the string is valid, False otherwise.
    """
    if not allow_empty and not input_string:
        return False
    if len(input_string) < min_length or len(input_string) > max_length:
        return False
    return True


def validate_integer(input_integer, min_value=None, max_value=None):
    """
    Validate an integer.

    Args:
        input_integer (int): The input integer to validate.
        min_value (int, optional): The minimum value of the integer. Defaults to None.
        max_value (int, optional): The maximum value of the integer. Defaults to None.

    Returns:
        bool: True if the integer is valid, False otherwise.
    """
    if not isinstance(input_integer, int):
        return False
    if min_value is not None and input_integer < min_value:
        return False
    if max_value is not None and input_integer > max_value:
        return False
    return True


def validate_email(input_email):
    """
    Validate an email address.

    Args:
        input_email (str): The input email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, input_email))


def validate_dict(input_dict, required_keys=None):
    """
    Validate a dictionary.

    Args:
        input_dict (dict): The input dictionary to validate.
        required_keys (list, optional): The required keys in the dictionary. Defaults to None.

    Returns:
        bool: True if the dictionary is valid, False otherwise.
    """
    if not isinstance(input_dict, dict):
        return False
    if required_keys is not None and not all(key in input_dict for key in required_keys):
        return False
    return True
```
