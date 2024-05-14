#Source: https://stackoverflow.com/questions/56261606/how-to-fix-typeerror-a-bytes-like-object-is-required-not-str-error-in-pyth
# mainTest.py module
from config import logger
log = logger.getLogger(__file__)

def function():
    message = "testing"
    log.info(message)
    # code