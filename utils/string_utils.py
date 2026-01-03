```python
"""
String utility functions for general use.
"""

import re

def to_title_case(input_string: str) -> str:
    """
    Converts a string to title case.

    Args:
        input_string (str): The string to convert.

    Returns:
        str: The input string in title case.
    """
    return input_string.title()

def remove_special_chars(input_string: str) -> str:
    """
    Removes special characters from a string.

    Args:
        input_string (str): The string to clean.

    Returns:
        str: The input string with special characters removed.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

def slugify(input_string: str) -> str:
    """
    Converts a string to a slug (lowercase, no spaces, no special characters).

    Args:
        input_string (str): The string to slugify.

    Returns:
        str: The input string as a slug.
    """
    return re.sub(r'[^a-zA-Z0-9]', '-', input_string.lower()).strip('-')

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates a string to a maximum length.

    Args:
        input_string (str): The string to truncate.
        max_length (int): The maximum length of the string.

    Returns:
        str: The input string truncated to the maximum length.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + '...'
    return input_string

# Example usage:
if __name__ == "__main__":
    print(to_title_case("hello world"))  # Output: Hello World
    print(remove_special_chars("Hello, World!"))  # Output: Hello World
    print(slugify("Hello, World!"))  # Output: hello-world
    print(truncate_string("This is a very long string", 10))  # Output: This is a...
```
