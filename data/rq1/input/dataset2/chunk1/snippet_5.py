#Source: https://stackoverflow.com/questions/68439799/typeerror-missing-1-required-positional-argument-while-using-pytest-fixture
import unittest
import pytest

@pytest.fixture
def base_value():
    return 5

class Test(unittest.TestCase):

    def test_add_two(self, base_value):
        result = base_value + 2
        self.assertEqual(result, 7, "Result doesn't match")