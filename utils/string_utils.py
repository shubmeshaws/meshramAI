```python
"""
String utility functions for meshram project.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
    email (str): Email address to be validated.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def remove_special_chars(input_str: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_str (str): Input string to remove special characters from.

    Returns:
    str: String with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_str)

def truncate_string(input_str: str, max_length: int) -> str:
    """
    Truncate a string to a specified length.

    Args:
    input_str (str): Input string to be truncated.
    max_length (int): Maximum length of the output string.

    Returns:
    str: Truncated string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + "..."
    return input_str

def camel_case_to_snake_case(input_str: str) -> str:
    """
    Convert a camel case string to snake case.

    Args:
    input_str (str): Input string in camel case.

    Returns:
    str: String in snake case.
    """
    snake_case_str = re.sub(r'(?<!^)(?=[A-Z])', '_', input_str).lower()
    return snake_case_str
```
