#Source: https://stackoverflow.com/questions/60542851/nameerror-name-method-name-is-not-defined-python-unittest
import unittest

from dir import *

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()