# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12332975/installing-python-module-within-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(1539877)

except ImportError:
    pass
try:
    import subprocess
    _l_(1539879)

except ImportError:
    pass
try:
    import pkg_resources
    _l_(1539881)

except ImportError:
    pass
try:
    from pkg_resources import DistributionNotFound, VersionConflict
    _l_(1539883)

except ImportError:
    pass

def should_install_requirement(requirement):
    _l_(1539897)

    should_install = False
    _l_(1539884)
    try:
        _l_(1539894)

        _c_(1539888, _a_(1539886, _n_(1539885, "pkg_resources", lambda: pkg_resources), "require"), _n_(1539887, "requirement", lambda: requirement))
        _l_(1539889)
    except (_n_(1539890, "DistributionNotFound", lambda: DistributionNotFound), _n_(1539891, "VersionConflict", lambda: VersionConflict)):
        _l_(1539893)

        should_install = True
        _l_(1539892)
    aux = _n_(1539895, "should_install", lambda: should_install)
    _l_(1539896)
    return aux


def install_packages(requirement_list):
    _l_(1539925)

    try:
        _l_(1539924)

        requirements = [
            _n_(1539898, "requirement", lambda: requirement)
            for requirement in _n_(1539899, "requirement_list", lambda: requirement_list)
            if _c_(1539902, _n_(1539900, "should_install_requirement", lambda: should_install_requirement), _n_(1539901, "requirement", lambda: requirement))
        ]
        _l_(1539903)
        if _c_(1539906, _n_(1539904, "len", lambda: len), _n_(1539905, "requirements", lambda: requirements)) > 0:
            _l_(1539917)

            _c_(1539912, _a_(1539908, _n_(1539907, "subprocess", lambda: subprocess), "check_call"), [_a_(1539910, _n_(1539909, "sys", lambda: sys), "executable"), "-m", "pip", "install", *_n_(1539911, "requirements", lambda: requirements)])
            _l_(1539913)
        else:
            _c_(1539915, _n_(1539914, "print", lambda: print), "Requirements already satisfied.")
            _l_(1539916)

    except _n_(1539918, "Exception", lambda: Exception) as e:
        _l_(1539923)

        _c_(1539921, _n_(1539919, "print", lambda: print), _n_(1539920, "e", lambda: e))
        _l_(1539922)

requirement_list = ['requests', 'httpx==0.18.2']
_l_(1539926)
_c_(1539929, _n_(1539927, "install_packages", lambda: install_packages), _n_(1539928, "requirement_list", lambda: requirement_list))
_l_(1539930)

