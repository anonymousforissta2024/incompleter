#Source: https://stackoverflow.com/questions/55131484/python-unittest-typeerror
import unittest
from MyCosine import CosineSim, CosineDis

class TestMyCosine(unittest.TestCase):

    x = [3.5 , 3 , 3.5 , 2.5 , 3]
    y = [3.5 , 3 , 4 , 2.5 , 4.5]
    result = 0.9865867

    def testCosineSim(self, result, x, y):
        self.x = x
        self.y = y
        self.result = result
        self.assertEqual(CosineSim(x,y), result, "0.9865867" )

    def testCosineDis(self, result, x, y):
        self.x = x
        self.y = y
        self.result = result
        self.assertEqual(CosineDis(x,y) , result, "0.9865867")


if __name__ == '__main__':
    unittest.main(exit=False)