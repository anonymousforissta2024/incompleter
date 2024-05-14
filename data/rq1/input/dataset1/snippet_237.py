# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class FlagAction(_a_(1541971, _n_(1541970, "argparse", lambda: argparse), "Action")):
    _l_(1542045)

    # From http://bugs.python.org/issue8538

    def __init__(self, option_strings, dest, default=None,
                 required=False, help=None, metavar=None,
                 positive_prefixes=['--'], negative_prefixes=['--no-']):
        _l_(1542027)

        _n_(1541972, "self", lambda: self).positive_strings = _c_(1541974, _n_(1541973, "set", lambda: set))
        _l_(1541975)
        _n_(1541976, "self", lambda: self).negative_strings = _c_(1541978, _n_(1541977, "set", lambda: set))
        _l_(1541979)
        for string in _n_(1541980, "option_strings", lambda: option_strings):
            _l_(1542006)

            assert _c_(1541984, _a_(1541982, _n_(1541981, "re", lambda: re), "match"), r'--[A-z]+', _n_(1541983, "string", lambda: string))
            _l_(1541985)
            suffix = _n_(1541986, "string", lambda: string)[2:]
            _l_(1541987)
            for positive_prefix in _n_(1541988, "positive_prefixes", lambda: positive_prefixes):
                _l_(1541996)

                _c_(1541994, _a_(1541991, _a_(1541990, _n_(1541989, "self", lambda: self), "positive_strings"), "add"), _n_(1541992, "positive_prefix", lambda: positive_prefix) + _n_(1541993, "suffix", lambda: suffix))
                _l_(1541995)
            for negative_prefix in _n_(1541997, "negative_prefixes", lambda: negative_prefixes):
                _l_(1542005)

                _c_(1542003, _a_(1542000, _a_(1541999, _n_(1541998, "self", lambda: self), "negative_strings"), "add"), _n_(1542001, "negative_prefix", lambda: negative_prefix) + _n_(1542002, "suffix", lambda: suffix))
                _l_(1542004)
        strings = _c_(1542012, _n_(1542007, "list", lambda: list), _a_(1542009, _n_(1542008, "self", lambda: self), "positive_strings") | _a_(1542011, _n_(1542010, "self", lambda: self), "negative_strings"))
        _l_(1542013)
        _c_(1542025, _a_(1542017, _n_(1542014, "super", lambda: super)(_n_(1542015, "FlagAction", lambda: FlagAction), _n_(1542016, "self", lambda: self)), "__init__"), option_strings=_n_(1542018, "strings", lambda: strings), dest=_n_(1542019, "dest", lambda: dest),
                                         nargs=0, const=None, default=_n_(1542020, "default", lambda: default), type=_n_(1542021, "bool", lambda: bool), choices=None,
                                         required=_n_(1542022, "required", lambda: required), help=_n_(1542023, "help", lambda: help), metavar=_n_(1542024, "metavar", lambda: metavar))
        _l_(1542026)

    def __call__(self, parser, namespace, values, option_string=None):
        _l_(1542044)

        if _n_(1542028, "option_string", lambda: option_string) in _a_(1542030, _n_(1542029, "self", lambda: self), "positive_strings"):
            _l_(1542043)

            _c_(1542035, _n_(1542031, "setattr", lambda: setattr), _n_(1542032, "namespace", lambda: namespace), _a_(1542034, _n_(1542033, "self", lambda: self), "dest"), True)
            _l_(1542036)
        else:
            _c_(1542041, _n_(1542037, "setattr", lambda: setattr), _n_(1542038, "namespace", lambda: namespace), _a_(1542040, _n_(1542039, "self", lambda: self), "dest"), False)
            _l_(1542042)

