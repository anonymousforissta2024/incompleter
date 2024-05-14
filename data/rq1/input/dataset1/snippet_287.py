# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import glob
    _l_(1539009)

except ImportError:
    pass
try:
    import os
    _l_(1539011)

except ImportError:
    pass

#to get the current working directory name
cwd = _c_(1539014, _a_(1539013, _n_(1539012, "os", lambda: os), "getcwd"))
_l_(1539015)
#Load the images from images folder.
for f in _c_(1539018, _a_(1539017, _n_(1539016, "glob", lambda: glob), "glob"), 'images\*.jpg'):
    _l_(1539029)

    dir_name = _c_(1539021, _n_(1539019, "get_dir_name", lambda: get_dir_name), _n_(1539020, "f", lambda: f))
    _l_(1539022)
    image_file_name = _n_(1539023, "dir_name", lambda: dir_name) + '.jpg'
    _l_(1539024)
    #To print the file name with path (path will be in string)
    _c_(1539027, _n_(1539025, "print", lambda: print), _n_(1539026, "image_file_name", lambda: image_file_name))
    _l_(1539028)

_c_(1539033, _a_(1539031, _n_(1539030, "os", lambda: os), "listdir"), _n_(1539032, "directory", lambda: directory))
_l_(1539034)

