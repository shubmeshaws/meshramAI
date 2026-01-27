```python
"""
String utility functions.

This module provides functions for common string operations such as trimming, padding, and formatting.
"""

import re

def trim_string(input_str, trim_chars=' \t\r\n'):
    """
    Trim leading and trailing characters from a string.

    Args:
        input_str (str): The input string to trim.
        trim_chars (str, optional): The characters to trim. Defaults to ' \t\r\n'.

    Returns:
        str: The trimmed string.
    """
    return input_str.strip(trim_chars)

def pad_string(input_str, pad_char=' ', pad_length=10):
    """
    Pad a string with a specified character to a specified length.

    Args:
        input_str (str): The input string to pad.
        pad_char (str, optional): The character to use for padding. Defaults to ' '.
        pad_length (int, optional): The desired length of the padded string. Defaults to 10.

    Returns:
        str: The padded string.
    """
    return input_str.ljust(pad_length, pad_char)

def format_string(input_str, **kwargs):
    """
    Format a string using keyword arguments.

    Args:
        input_str (str): The input string to format.
        **kwargs: Keyword arguments to use for formatting.

    Returns:
        str: The formatted string.
    """
    return input_str.format(**kwargs)

def extract_pattern(input_str, pattern):
    """
    Extract a pattern from a string using regular expressions.

    Args:
        input_str (str): The input string to extract from.
        pattern (str): The regular expression pattern to match.

    Returns:
        list: A list of matches.
    """
    return re.findall(pattern, input_str)

def replace_pattern(input_str, pattern, replacement):
    """
    Replace a pattern in a string using regular expressions.

    Args:
        input_str (str): The input string to replace in.
        pattern (str): The regular expression pattern to match.
        replacement (str): The replacement string.

    Returns:
        str: The modified string.
    """
    return re.sub(pattern, replacement, input_str)
```
