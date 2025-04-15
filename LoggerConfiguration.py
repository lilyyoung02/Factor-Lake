import logging
import sys

def get_logger(name=None):
    root_logger = logging.getLogger()
    if not root_logger.handlers:
        handler = logging.StreamHandler(sys.stdout)  # force stdout for Colab
        formatter = logging.Formatter('%(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        root_logger.addHandler(handler)

    return logging.getLogger(name)
