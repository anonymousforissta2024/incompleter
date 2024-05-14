#Source: https://stackoverflow.com/questions/44011169/python-pycharm-file-structure-issue-attributeerror-module-object-has-no-at
import unittest
import os, sys
import gmpy2
from gmpy2 import mpz

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Utils.Utils           import AssertInt, AssertClass
from Utils.ToInteger       import ToInteger
from Utils.RecHash         import RecHash    

def GetGenerators(n):
    AssertInt(n)
    assert n >= 0, "n must be greater than or equal 0"

    generators = []

    # ... irrelevant code...

    return generators


class GetGeneratorsTest(unittest.TestCase):
    def testGetGenerators(self):
        self.assertEqual(len(GetGenerators(50)), 50)


if __name__ == '__main__':
    unittest.main()