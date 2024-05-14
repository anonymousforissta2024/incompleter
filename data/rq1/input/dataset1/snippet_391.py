# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5191830/how-do-i-log-a-python-error-with-debug-information
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import logging
    _l_(1545286)

except ImportError:
    pass
try:
    from contextlib import AbstractContextManager
    _l_(1545288)

except ImportError:
    pass


class LogError(_n_(1545289, "AbstractContextManager", lambda: AbstractContextManager)):
    _l_(1545313)


    def __init__(self, logger=None):
        _l_(1545300)

        _n_(1545290, "self", lambda: self).logger = _a_(1545292, _n_(1545291, "logger", lambda: logger), "name") if _c_(1545297, _n_(1545293, "isinstance", lambda: isinstance), _n_(1545294, "logger", lambda: logger), _a_(1545296, _n_(1545295, "logging", lambda: logging), "Logger")) else _n_(1545298, "logger", lambda: logger)
        _l_(1545299)

    def __exit__(self, exc_type, exc_value, traceback):
        _l_(1545312)

        if _n_(1545301, "exc_value", lambda: exc_value) is not None:
            _l_(1545311)

            _c_(1545309, _a_(1545307, _c_(1545306, _a_(1545303, _n_(1545302, "logging", lambda: logging), "getLogger"), _a_(1545305, _n_(1545304, "self", lambda: self), "logger")), "exception"), _n_(1545308, "exc_value", lambda: exc_value))
            _l_(1545310)


with _c_(1545315, _n_(1545314, "LogError", lambda: LogError)):
    _l_(1545317)

    1/0
    _l_(1545316)

