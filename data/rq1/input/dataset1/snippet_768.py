# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2759067/rename-multiple-files-in-a-directory-in-python
#List all files in the directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
file_list = _c_(1539099, _a_(1539098, _n_(1539097, "os", lambda: os), "listdir"), "/Users/tedfuller/Desktop/prank/")
_l_(1539100)
_c_(1539103, _n_(1539101, "print", lambda: print), _n_(1539102, "file_list", lambda: file_list))
_l_(1539104)

#Change current working directory and print out it's location
working_location = _c_(1539107, _a_(1539106, _n_(1539105, "os", lambda: os), "chdir"), "/Users/tedfuller/Desktop/prank/")
_l_(1539108)
working_location = _c_(1539111, _a_(1539110, _n_(1539109, "os", lambda: os), "getcwd"))
_l_(1539112)
_c_(1539115, _n_(1539113, "print", lambda: print), _n_(1539114, "working_location", lambda: working_location))
_l_(1539116)

#Rename all the files in that directory
for file_name in _n_(1539117, "file_list", lambda: file_list):
    _l_(1539131)

    _c_(1539129, _a_(1539119, _n_(1539118, "os", lambda: os), "rename"), _n_(1539120, "file_name", lambda: file_name), _c_(1539128, _a_(1539122, _n_(1539121, "file_name", lambda: file_name), "translate"), _c_(1539127, _a_(1539124, _n_(1539123, "str", lambda: str), "maketrans"), "","",_a_(1539126, _n_(1539125, "string", lambda: string), "digits"))))
    _l_(1539130)

