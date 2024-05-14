#Source: https://stackoverflow.com/questions/60541782/attributeerror-when-patching-class-variable-when-mocking
import unittest
from unittest.mock import patch
from unittest.mock import Mock
from mocking_module import class_util


class TestSomething(unittest.TestCase):

    @patch.object("mocking_module.class_util.SampleClass", "base_url", "http://override.com")
    def test_class_variable_override(self):

        print("url = {}".format(class_util.do_something()))