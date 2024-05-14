#Source: https://stackoverflow.com/questions/40243193/getting-python-error-typeerror-nonetype-object-is-not-callable-sometimes
import unittest

from nose_parameterized import parameterized
from CheckFromFile import listFileCheck, RepresentsFloat

testParams = listFileCheck()


class TestSequence(unittest.TestCase):

    @parameterized.expand(testParams)
    def test_sequence(self, name, a, b):
        if RepresentsFloat(a):
            self.assertAlmostEqual(a,b,2)
        else:
            self.assertEqual(a,b)


if __name__ == '__main__':
    unittest.main()