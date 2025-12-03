```python
import logging
import os

# Set up logging configuration
LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')

# Validate the LOGGING_LEVEL environment variable
valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
if LOGGING_LEVEL.upper() not in valid_levels:
    print(f"Invalid LOGGING_LEVEL: {LOGGING_LEVEL}. Defaulting to INFO.")
    LOGGING_LEVEL = 'INFO'

try:
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=getattr(logging, LOGGING_LEVEL.upper())
    )
except Exception as e:
    print(f"Error setting up logging: {str(e)}")

class Logger:
    def __init__(self, name):
        try:
            self.logger = logging.getLogger(name)
        except Exception as e:
            print(f"Error creating logger: {str(e)}")

    def info(self, message):
        try:
            self.logger.info(message)
        except Exception as e:
            print(f"Error logging info message: {str(e)}")

    def error(self, message):
        try:
            self.logger.error(message)
        except Exception as e:
            print(f"Error logging error message: {str(e)}")

    def debug(self, message):
        try:
            self.logger.debug(message)
        except Exception as e:
            print(f"Error logging debug message: {str(e)}")

    def warn(self, message):
        try:
            self.logger.warning(message)
        except Exception as e:
            print(f"Error logging warning message: {str(e)}")

def get_logger(name):
    return Logger(name)

# Example usage:
# logger = get_logger(__name__)
# logger.info('This is an info message')
# logger.error('This is an error message')
```
