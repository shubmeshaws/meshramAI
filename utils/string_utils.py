```python
"""
Utility functions for string manipulation and formatting.
"""

def truncate_string(input_str, max_length):
    """
    Truncates a string to a specified maximum length.

    Args:
        input_str (str): The input string to be truncated.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The truncated string.
    """
    if len(input_str) <= max_length:
        return input_str
    else:
        return input_str[:max_length - 3] + "..."

def remove_special_chars(input_str):
    """
    Removes special characters from a string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The string without special characters.
    """
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

def to_title_case(input_str):
    """
    Converts a string to title case.

    Args:
        input_str (str): The input string.

    Returns:
        str: The string in title case.
    """
    return input_str.title()

def format_string(input_str, **kwargs):
    """
    Formats a string using keyword arguments.

    Args:
        input_str (str): The input string.
        **kwargs: Keyword arguments to be used in string formatting.

    Returns:
        str: The formatted string.
    """
    return input_str.format(**kwargs)

# Example usage:
if __name__ == "__main__":
    print(truncate_string("This is a very long string", 20))
    print(remove_special_chars("Hello, World!"))
    print(to_title_case("hello world"))
    print(format_string("My name is {name}", name="John"))
```
