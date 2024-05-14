#Source: https://stackoverflow.com/questions/51846824/using-unittest-mock-patch-dict-on-os-environ-is-resulting-in-a-typeerror
import os
from unittest.mock import patch
with patch.dict('os.environ', values={"foo": 3, "bar": "hello"}, clear=True):
    print(os.environ["foo"])
    print(os.environ["bar"])