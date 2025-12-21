```python
"""
String utility functions.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if the input string is empty or contains only whitespace characters.

    Args:
    input_string (str): The input string to check.

    Returns:
    bool: True if the string is empty, False otherwise.
    """
    return not input_string.strip()

def validate_email(input_string: str) -> bool:
    """
    Validates if the input string is a valid email address.

    Args:
    input_string (str): The input string to validate.

    Returns:
    bool: True if the string is a valid email address, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, input_string))

def remove_special_chars(input_string: str) -> str:
    """
    Removes all special characters from the input string.

    Args:
    input_string (str): The input string to process.

    Returns:
    str: The input string without special characters.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates the input string to the specified maximum length.

    Args:
    input_string (str): The input string to truncate.
    max_length (int): The maximum length of the output string.

    Returns:
    str: The truncated input string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string

# Example usage:
if __name__ == "__main__":
    print(is_empty_string(""))  # Output: True
    print(validate_email("example@example.com"))  # Output: True
    print(remove_special_chars("Hello, World!"))  # Output: "HelloWorld"
    print(truncate_string("This is a very long string", 10))  # Output: "This is a..."
```
