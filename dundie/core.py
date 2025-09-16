"""Core module of dundie."""
from dundie.utils.log import get_logger
log = get_logger()


def load(filepath):
    """Loads data from a filepath to the database.
    >>> load('assets/employees.csv')[0].startswith('Jim')
    True
    >>> len(load('assets/employees.csv'))
    2
    """
    try:
        with open(filepath) as file_:
            return file_.readlines()                
    except FileNotFoundError as e:
        log.error(str(e))
        raise e
