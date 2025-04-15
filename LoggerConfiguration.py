import logging

def get_logger(name=None, level=None):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    if level is not None:
        logger.setLevel(level)
    return logger
