```python
import os

def check_file_exists(file_path):
    """
    Check if a file exists.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

def create_directory(dir_path):
    """
    Create a directory if it does not exist.

    Args:
        dir_path (str): The path to the directory.

    Returns:
        None
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def delete_file(file_path):
    """
    Delete a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        None
    """
    if check_file_exists(file_path):
        os.remove(file_path)

def delete_directory(dir_path):
    """
    Delete a directory and its contents.

    Args:
        dir_path (str): The path to the directory.

    Returns:
        None
    """
    if os.path.exists(dir_path):
        import shutil
        shutil.rmtree(dir_path)
```
