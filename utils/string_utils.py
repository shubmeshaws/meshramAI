```python
# utils/string_utils.py

"""
Utility functions for common string operations.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Check if a string is empty or contains only whitespace characters.
    
    Args:
        input_string (str): The string to check.
    
    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validate an email address using a regular expression.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def format_string(input_string: str, **kwargs) -> str:
    """
    Format a string using keyword arguments.
    
    Args:
        input_string (str): The string to format.
        **kwargs: Keyword arguments to replace in the string.
    
    Returns:
        str: The formatted string.
    """
    return input_string.format(**kwargs)

def remove_special_characters(input_string: str) -> str:
    """
    Remove special characters from a string.
    
    Args:
        input_string (str): The string to clean.
    
    Returns:
        str: The cleaned string.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

def camel_case_to_snake_case(input_string: str) -> str:
    """
    Convert a camel case string to snake case.
    
    Args:
        input_string (str): The string to convert.
    
    Returns:
        str: The converted string.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_string).lower()
```
