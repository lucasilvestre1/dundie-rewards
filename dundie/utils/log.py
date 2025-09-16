import os
import logging
from logging import handlers


LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.getLogger("dundie")
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)


def get_logger(log_file="dundie.log"):
    """Returns a configured logger."""
    #ch = logging.StreamHandler()  # Console/terminal/stderr
    #ch.setLevel(log_level)
    fh = handlers.RotatingFileHandler(
        log_file, 
        maxBytes=300, # 10**6 (1MB)
        backupCount=10,  # num backup files
    )
    fh.setLevel(LOG_LEVEL)
    # ch.setFormatter(fmt)
    fh.setFormatter(fmt)
    #log.addHandler(ch)
    log.addHandler(fh)
    return log
