import logging
import os

def setup_logger():
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # File handler to log API calls and errors
        log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "trading_bot.log")
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)
        
        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        
        logger.addHandler(fh)
        
    return logger

logger = setup_logger()
