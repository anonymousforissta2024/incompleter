#Source: https://stackoverflow.com/questions/49469481/lpthw-48-nosetest-says-attributeerror-str-object-has-no-attribute-while
from nose.tools import *
from ex48 import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])