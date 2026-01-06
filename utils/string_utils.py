```python
"""
Utility functions for common string operations.
"""

def camel_case_to_snake_case(input_string):
    """
    Convert a camel case string to snake case.
    
    Args:
        input_string (str): The input string in camel case.
    
    Returns:
        str: The input string converted to snake case.
    """
    words = []
    word = ""
    for char in input_string:
        if char.isupper():
            if word:
                words.append(word)
            word = char.lower()
        else:
            word += char
    if word:
        words.append(word)
    return "_".join(words)


def snake_case_to_camel_case(input_string):
    """
    Convert a snake case string to camel case.
    
    Args:
        input_string (str): The input string in snake case.
    
    Returns:
        str: The input string converted to camel case.
    """
    words = input_string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])


def trim_string(input_string, max_length):
    """
    Trim a string to a specified maximum length.
    
    Args:
        input_string (str): The input string to be trimmed.
        max_length (int): The maximum allowed length of the string.
    
    Returns:
        str: The input string trimmed to the specified maximum length.
    """
    if len(input_string) > max_length:
        return input_string[:max_length - 3] + "..."
    return input_string


def is_empty_string(input_string):
    """
    Check if a string is empty or contains only whitespace characters.
    
    Args:
        input_string (str): The input string to be checked.
    
    Returns:
        bool: True if the string is empty or contains only whitespace characters, False otherwise.
    """
    return not input_string.strip()
```
