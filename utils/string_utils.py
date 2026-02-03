```python
import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if the input string is empty or contains only whitespace.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return not input_string.strip()

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

def validate_ip_address(ip_address: str) -> bool:
    """
    Validates an IP address using a regular expression.

    Args:
        ip_address (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return bool(re.match(ip_address_regex, ip_address))

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
        return input_string[:max_length - 3] + "..."
    return input_string
```
