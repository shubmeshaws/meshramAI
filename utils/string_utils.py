```python
"""
String utility functions.
"""

import re

def is_empty(string: str) -> bool:
    """
    Checks if a string is empty or contains only whitespace characters.
    
    Args:
    string (str): The input string to check.
    
    Returns:
    bool: True if the string is empty, False otherwise.
    """
    return not string.strip()

def validate_email(email: str) -> bool:
    """
    Validates an email address using a regular expression.
    
    Args:
    email (str): The email address to validate.
    
    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates a string to a specified maximum length.
    
    Args:
    input_string (str): The string to truncate.
    max_length (int): The maximum length of the output string.
    
    Returns:
    str: The truncated string.
    """
    if len(input_string) <= max_length:
        return input_string
    else:
        return input_string[:max_length - 3] + "..."

def remove_special_chars(input_string: str) -> str:
    """
    Removes special characters from a string.
    
    Args:
    input_string (str): The string to remove special characters from.
    
    Returns:
    str: The string without special characters.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)

def convert_to_snake_case(input_string: str) -> str:
    """
    Converts a string to snake case.
    
    Args:
    input_string (str): The string to convert.
    
    Returns:
    str: The string in snake case.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_string).lower()
```
