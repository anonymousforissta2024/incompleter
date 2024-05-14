# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3451111/unzipping-files-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import zipfile
    _l_(1540701)

except ImportError:
    pass
with _c_(1540704, _a_(1540703, _n_(1540702, "zipfile", lambda: zipfile), "ZipFile"), "file.zip","r") as zip_ref:
    _l_(1540709)

    _c_(1540707, _a_(1540706, _n_(1540705, "zip_ref", lambda: zip_ref), "extractall"), "targetdir")
    _l_(1540708)

