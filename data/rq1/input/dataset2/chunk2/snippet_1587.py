#Source: https://stackoverflow.com/questions/42932773/setting-up-a-simple-python-app-with-pytest-getting-error-nameerror-and-attribute
# content of test_app.py
import pytest
import mypkg

def test_answer():
    assert func(4) == 5