#Source: https://stackoverflow.com/questions/57890868/vscode-pytest-error-typeerror-cannot-read-property-of-undefined
import inc_dec    # The code to test

def test_increment():
    assert inc_dec.increment(3) == 4

def test_decrement():
    assert inc_dec.decrement(3) == 4