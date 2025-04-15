import logging

def get_logger(name=None, level=logging.INFO):
    logger = logging.getLogger(name)
    
    # If no handlers, set one
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        handler.setLevel(level)  
        logger.addHandler(handler)
    
    logger.setLevel(level)  # Logger level
    return logger
