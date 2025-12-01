```python
import logging
import os

# Set up logging configuration
LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')

logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=getattr(logging, LOGGING_LEVEL.upper())
)

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

    def warn(self, message):
        self.logger.warning(message)

def get_logger(name):
    return Logger(name)

# Example usage:
# logger = get_logger(__name__)
# logger.info('This is an info message')
# logger.error('This is an error message')
```
```
