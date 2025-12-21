```python
import logging
import os

# Set up logging configuration
LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')

# Validate the LOGGING_LEVEL environment variable
valid_levels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}

if LOGGING_LEVEL.upper() not in valid_levels:
    logging.warning(f"Invalid LOGGING_LEVEL: {LOGGING_LEVEL}. Defaulting to INFO.")
    LOGGING_LEVEL = 'INFO'

logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=valid_levels[LOGGING_LEVEL.upper()]
)

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def log(self, level, message):
        level_func = getattr(self.logger, level.lower())
        level_func(message)

    def info(self, message):
        self.log('INFO', message)

    def error(self, message):
        self.log('ERROR', message)

    def debug(self, message):
        self.log('DEBUG', message)

    def warn(self, message):
        self.log('WARNING', message)

def get_logger(name):
    return Logger(name)

# Example usage:
# logger = get_logger(__name__)
# logger.info('This is an info message')
# logger.error('This is an error message')
```
