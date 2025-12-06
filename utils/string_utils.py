```python
"""
String utility functions.

This module provides various functions for string manipulation and formatting.
"""

import re
from typing import List, Tuple

def camel_case_to_snake_case(input_string: str) -> str:
    """
    Converts a camel case string to snake case.

    Args:
        input_string (str): The input string in camel case.

    Returns:
        str: The input string converted to snake case.
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def snake_case_to_camel_case(input_string: str) -> str:
    """
    Converts a snake case string to camel case.

    Args:
        input_string (str): The input string in snake case.

    Returns:
        str: The input string converted to camel case.
    """
    words = input_string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])


def split_string(input_string: str, delimiter: str, max_split: int = -1) -> List[str]:
    """
    Splits a string into a list of substrings based on a delimiter.

    Args:
        input_string (str): The input string to be split.
        delimiter (str): The delimiter used to split the string.
        max_split (int): The maximum number of splits. Defaults to -1.

    Returns:
        List[str]: A list of substrings.
    """
    return input_string.split(delimiter, max_split)


def remove_whitespace(input_string: str) -> str:
    """
    Removes leading and trailing whitespace from a string.

    Args:
        input_string (str): The input string.

    Returns:
        str: The input string with leading and trailing whitespace removed.
    """
    return input_string.strip()


def extract_numbers(input_string: str) -> List[int]:
    """
    Extracts numbers from a string.

    Args:
        input_string (str): The input string.

    Returns:
        List[int]: A list of extracted numbers.
    """
    return [int(num) for num in re.findall(r'\d+', input_string)]


def tuple_to_string(input_tuple: Tuple, delimiter: str = ', ') -> str:
    """
    Converts a tuple to a string.

    Args:
        input_tuple (Tuple): The input tuple.
        delimiter (str): The delimiter used to join the elements. Defaults to ', '.

    Returns:
        str: A string representation of the tuple.
    """
    return delimiter.join(str(element) for element in input_tuple)
```
