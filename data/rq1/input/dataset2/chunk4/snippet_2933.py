#Source: https://stackoverflow.com/questions/69839628/attributeerror-nonetype-object-has-no-attribute-dropna
import unittest
from src.numeric import NumericColumn
import pandas as pd

class TestNumeric(unittest.TestCase):  
    def test_numeric(self):
        ### test on dummy data ###
        # create series of data
        dc1 = NumericColumn()
        dc1.col_name = "my_test"

        # test methods
        self.assertEqual(dc1.get_name(),"my_test")
        self.assertEqual(dc1.get_unique(),7)
        self.assertEqual(dc1.get_missing(),1)