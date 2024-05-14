# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/67631/how-can-i-import-a-module-dynamically-given-the-full-path
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
path = _c_(1548610, _a_(1548609, _a_(1548608, _n_(1548607, "os", lambda: os), "path"), "join"), './path/to/folder/with/py/files', '*.py')
_l_(1548611)
for infile in _c_(1548615, _a_(1548613, _n_(1548612, "glob", lambda: glob), "glob"), _n_(1548614, "path", lambda: path)):
    _l_(1548630)

    basename = _c_(1548620, _a_(1548618, _a_(1548617, _n_(1548616, "os", lambda: os), "path"), "basename"), _n_(1548619, "infile", lambda: infile))
    _l_(1548621)
    basename_without_extension = _n_(1548622, "basename", lambda: basename)[:-3]
    _l_(1548623)

    # http://docs.python.org/library/imp.html?highlight=imp#module-imp
    _c_(1548628, _a_(1548625, _n_(1548624, "imp", lambda: imp), "load_source"), _n_(1548626, "basename_without_extension", lambda: basename_without_extension), _n_(1548627, "infile", lambda: infile))
    _l_(1548629)

