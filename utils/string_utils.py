```python
import re

def is_valid_email(email: str) -> bool:
    """
    Checks if the provided email address is valid.
    
    Args:
    email (str): The email address to validate.
    
    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def is_valid_ip_address(ip_address: str) -> bool:
    """
    Checks if the provided IP address is valid.
    
    Args:
    ip_address (str): The IP address to validate.
    
    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    ip_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_regex, ip_address))

def remove_special_chars(input_string: str) -> str:
    """
    Removes special characters from the input string.
    
    Args:
    input_string (str): The string to remove special characters from.
    
    Returns:
    str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates the input string to the specified maximum length.
    
    Args:
    input_string (str): The string to truncate.
    max_length (int): The maximum length of the truncated string.
    
    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length - 3] + '...'
    return input_string
```
