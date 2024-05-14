# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9079036/how-do-i-detect-the-python-version-at-runtime
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def check_installation(rv):
    _l_(1546325)

    current_version = _a_(1546302, _n_(1546301, "sys", lambda: sys), "version_info")
    _l_(1546303)
    if _n_(1546304, "current_version", lambda: current_version)[0] == _n_(1546305, "rv", lambda: rv)[0] and _n_(1546306, "current_version", lambda: current_version)[1] >= _n_(1546307, "rv", lambda: rv)[1]:
        _l_(1546323)

        pass
        _l_(1546308)
    else:
        _c_(1546317, _a_(1546311, _a_(1546310, _n_(1546309, "sys", lambda: sys), "stderr"), "write"), "[%s] - Error: Your Python interpreter must be %d.%d or greater (within major version %d)\n" % (_a_(1546313, _n_(1546312, "sys", lambda: sys), "argv")[0], _n_(1546314, "rv", lambda: rv)[0], _n_(1546315, "rv", lambda: rv)[1], _n_(1546316, "rv", lambda: rv)[0]) )
        _l_(1546318)
        _c_(1546321, _a_(1546320, _n_(1546319, "sys", lambda: sys), "exit"), -1)
        _l_(1546322)
    aux = 0
    _l_(1546324)
    return aux


# Calling the 'check_installation' function checks if Python is >= 2.7 and < 3
required_version = (2,7)
_l_(1546326)
_c_(1546329, _n_(1546327, "check_installation", lambda: check_installation), _n_(1546328, "required_version", lambda: required_version))
_l_(1546330)

