#Source: https://stackoverflow.com/questions/61717953/pytest-custom-exception-typeerror-exceptions-must-be-derived-from-baseexcep
from pyupurs.exceptions import FileIsEmptyError

...

with pytest.raises(FileIsEmptyError):
    raise FileIsEmptyError