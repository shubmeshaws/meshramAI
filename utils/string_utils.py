```python
"""
String utility module for handling string operations.
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

def extract_substring(input_string: str, start: int, end: int) -> str:
    """
    Extracts a substring from the input string.
    
    Args:
    input_string (str): The input string.
    start (int): The start index of the substring.
    end (int): The end index of the substring.
    
    Returns:
    str: The extracted substring.
    """
    return input_string[start:end]

def replace_special_chars(input_string: str, replacement: str = "") -> str:
    """
    Replaces special characters in the input string with the specified replacement.
    
    Args:
    input_string (str): The input string.
    replacement (str): The replacement string. Defaults to an empty string.
    
    Returns:
    str: The input string with special characters replaced.
    """
    return re.sub(r"[^a-zA-Z0-9\s]", replacement, input_string)

def main():
    # Example usage
    email = "example@example.com"
    print(validate_email(email))  # Output: True
    
    input_string = "Hello, World!"
    print(replace_special_chars(input_string))  # Output: "Hello World"

if __name__ == "__main__":
    main()
```
