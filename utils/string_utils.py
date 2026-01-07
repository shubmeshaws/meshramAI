```python
"""
Utility functions for string manipulation.
"""

def to_snake_case(input_string: str) -> str:
    """
    Convert a string to snake case.
    
    Args:
    input_string (str): The input string to convert.
    
    Returns:
    str: The input string in snake case.
    """
    return input_string.replace(' ', '_').lower()


def to_camel_case(input_string: str) -> str:
    """
    Convert a string to camel case.
    
    Args:
    input_string (str): The input string to convert.
    
    Returns:
    str: The input string in camel case.
    """
    words = input_string.split(' ')
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])


def trim_string(input_string: str) -> str:
    """
    Trim leading and trailing whitespace from a string.
    
    Args:
    input_string (str): The input string to trim.
    
    Returns:
    str: The trimmed input string.
    """
    return input_string.strip()


def is_empty_string(input_string: str) -> bool:
    """
    Check if a string is empty.
    
    Args:
    input_string (str): The input string to check.
    
    Returns:
    bool: True if the input string is empty, False otherwise.
    """
    return len(trim_string(input_string)) == 0


def main():
    print(to_snake_case("Hello World"))  # Output: hello_world
    print(to_camel_case("hello world"))  # Output: helloWorld
    print(trim_string("   Hello World   "))  # Output: Hello World
    print(is_empty_string("   "))  # Output: True


if __name__ == "__main__":
    main()
```
