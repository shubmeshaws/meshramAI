```python
import re

def is_empty(string):
    """
    Checks if a string is empty.

    Args:
        string (str): The input string.

    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return not string.strip()

def validate_string(string, regex_pattern):
    """
    Validates a string against a regular expression pattern.

    Args:
        string (str): The input string.
        regex_pattern (str): The regular expression pattern.

    Returns:
        bool: True if the string matches the pattern, False otherwise.
    """
    return bool(re.match(regex_pattern, string))

def sanitize_string(string, allowed_chars):
    """
    Sanitizes a string by removing all characters not in the allowed set.

    Args:
        string (str): The input string.
        allowed_chars (str): The set of allowed characters.

    Returns:
        str: The sanitized string.
    """
    return ''.join(char for char in string if char in allowed_chars)

def format_string(string, **kwargs):
    """
    Formats a string using keyword arguments.

    Args:
        string (str): The input string.
        **kwargs: Keyword arguments for formatting.

    Returns:
        str: The formatted string.
    """
    return string.format(**kwargs)

def split_string(string, delimiter):
    """
    Splits a string into a list of substrings using a delimiter.

    Args:
        string (str): The input string.
        delimiter (str): The delimiter.

    Returns:
        list: A list of substrings.
    """
    return string.split(delimiter)

def join_strings(strings, delimiter):
    """
    Joins a list of strings into a single string using a delimiter.

    Args:
        strings (list): A list of strings.
        delimiter (str): The delimiter.

    Returns:
        str: The joined string.
    """
    return delimiter.join(strings)
```
