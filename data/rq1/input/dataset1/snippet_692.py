# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/22604564/create-pandas-dataframe-from-a-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import io
    _l_(1543356)

except ImportError:
    pass
try:
    import re
    _l_(1543358)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(1543360)

except ImportError:
    pass


def read_psv(str_input: _n_(1543361, "str", lambda: str), **kwargs) -> _a_(1543363, _n_(1543362, "pd", lambda: pd), "DataFrame"):
    _l_(1543407)

    """Read a Pandas object from a pipe-separated table contained within a string.

    Input example:
        | int_score | ext_score | eligible |
        |           | 701       | True     |
        | 221.3     | 0         | False    |
        |           | 576       | True     |
        | 300       | 600       | True     |

    The leading and trailing pipes are optional, but if one is present,
    so must be the other.

    `kwargs` are passed to `read_csv`. They must not include `sep`.

    In PyCharm, the "Pipe Table Formatter" plugin has a "Format" feature that can 
    be used to neatly format a table.

    Ref: https://stackoverflow.com/a/46471952/
    """

    substitutions = [
        ('^ *', ''),  # Remove leading spaces
        (' *$', ''),  # Remove trailing spaces
        (r' *\| *', '|'),  # Remove spaces between columns
    ]
    _l_(1543364)
    if _c_(1543381, _n_(1543365, "all", lambda: all), (_c_(1543370, _a_(1543369, _c_(1543368, _a_(1543367, _n_(1543366, "line", lambda: line), "lstrip")), "startswith"), '|') and _c_(1543375, _a_(1543374, _c_(1543373, _a_(1543372, _n_(1543371, "line", lambda: line), "rstrip")), "endswith"), '|') for line in _c_(1543380, _a_(1543379, _c_(1543378, _a_(1543377, _n_(1543376, "str_input", lambda: str_input), "strip")), "split"), '\n'))):
        _l_(1543386)

        _c_(1543384, _a_(1543383, _n_(1543382, "substitutions", lambda: substitutions), "extend"), [
            (r'^\|', ''),  # Remove redundant leading delimiter
            (r'\|$', ''),  # Remove redundant trailing delimiter
        ])
        _l_(1543385)
    for pattern, replacement in _n_(1543387, "substitutions", lambda: substitutions):
        _l_(1543397)

        str_input = _c_(1543395, _a_(1543389, _n_(1543388, "re", lambda: re), "sub"), _n_(1543390, "pattern", lambda: pattern), _n_(1543391, "replacement", lambda: replacement), _n_(1543392, "str_input", lambda: str_input), flags=_a_(1543394, _n_(1543393, "re", lambda: re), "MULTILINE"))
        _l_(1543396)
    aux = _c_(1543405, _a_(1543399, _n_(1543398, "pd", lambda: pd), "read_csv"), _c_(1543403, _a_(1543401, _n_(1543400, "io", lambda: io), "StringIO"), _n_(1543402, "str_input", lambda: str_input)), sep='|', **_n_(1543404, "kwargs", lambda: kwargs))
    _l_(1543406)
    return aux


df = _c_(1543414, _a_(1543409, _n_(1543408, "pd", lambda: pd), "read_csv"), _c_(1543413, _a_(1543411, _n_(1543410, "io", lambda: io), "StringIO"), _n_(1543412, "df_str", lambda: df_str)), sep=r'\s*\|\s*', engine='python')
_l_(1543415)

