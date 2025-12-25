```python
"""
String utility functions for string manipulation and validation.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate if the provided email address is valid.

    Args:
    email (str): The email address to be validated.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def remove_special_chars(input_string: str) -> str:
    """
    Remove special characters from the input string.

    Args:
    input_string (str): The input string to remove special characters from.

    Returns:
    str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)

def truncate_string(input_string: str, length: int) -> str:
    """
    Truncate the input string to the specified length.

    Args:
    input_string (str): The input string to be truncated.
    length (int): The maximum length of the output string.

    Returns:
    str: The truncated input string.
    """
    if len(input_string) > length:
        return input_string[:length] + "..."
    return input_string

def is_empty_or_whitespace(input_string: str) -> bool:
    """
    Check if the input string is empty or contains only whitespace characters.

    Args:
    input_string (str): The input string to be checked.

    Returns:
    bool: True if the input string is empty or contains only whitespace characters, False otherwise.
    """
    return not input_string.strip()

# Example usage
if __name__ == "__main__":
    print(validate_email("example@example.com"))  # True
    print(validate_email("invalid_email"))  # False
    print(remove_special_chars("Hello, World!"))  # "HelloWorld"
    print(truncate_string("This is a very long string", 10))  # "This is a..."
    print(is_empty_or_whitespace("   "))  # True
    print(is_empty_or_whitespace("not empty"))  # False
```
