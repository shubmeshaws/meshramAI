```python
"""
String utility functions.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate an email address.
    
    Args:
    email (str): The email address to validate.
    
    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def camel_case_to_snake_case(input_string: str) -> str:
    """
    Convert a camel case string to snake case.
    
    Args:
    input_string (str): The string to convert.
    
    Returns:
    str: The input string in snake case.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_string).lower()

def trim_string(input_string: str, max_length: int) -> str:
    """
    Trim a string to a specified length.
    
    Args:
    input_string (str): The string to trim.
    max_length (int): The maximum length of the string.
    
    Returns:
    str: The trimmed string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length - 3] + '...'
    return input_string

def is_empty_string(input_string: str) -> bool:
    """
    Check if a string is empty or contains only whitespace characters.
    
    Args:
    input_string (str): The string to check.
    
    Returns:
    bool: True if the string is empty, False otherwise.
    """
    return not input_string.strip()
```
