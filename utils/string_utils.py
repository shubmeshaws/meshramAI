```python
import re

def camel_to_snake_case(s):
    """
    Convert a camel case string to snake case.

    Args:
        s (str): The input string.

    Returns:
        str: The converted string.
    """
    return re.sub('([A-Z])', r'_\1', s).lower().lstrip('_')

def snake_to_camel_case(s):
    """
    Convert a snake case string to camel case.

    Args:
        s (str): The input string.

    Returns:
        str: The converted string.
    """
    components = s.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def truncate_string(s, length):
    """
    Truncate a string to a specified length.

    Args:
        s (str): The input string.
        length (int): The desired length.

    Returns:
        str: The truncated string.
    """
    if len(s) > length:
        return s[:length - 3] + '...'
    return s

def remove_special_chars(s):
    """
    Remove special characters from a string.

    Args:
        s (str): The input string.

    Returns:
        str: The cleaned string.
    """
    return re.sub('[^A-Za-z0-9]+', '', s)

def is_valid_email(email):
    """
    Check if a string is a valid email address.

    Args:
        email (str): The input string.

    Returns:
        bool: True if the string is a valid email address, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))
```
