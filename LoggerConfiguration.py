import logging

def get_logger(name=None, level=logging.INFO):
    logger = logging.getLogger(name)
    if not logger.handlers:  # Prevent duplicate handlers
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger
