#Source: https://stackoverflow.com/questions/40499916/htmltestrunner-error-raise-typeerror-is-not-callable-formatreprtest
import pymysql
import pymysql
import unittest
import time
import unittest.suite
import HTMLTestRunner
import sys
def hell(a):
    print(a)
    return a
testunit = unittest.TestSuite()
testunit.addTest(hell('ad'))
filename = '/Users/vivi/Downloads/aa.html'
fp = open(filename, 'wb')  
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'print', description=u'简单')
runner.run(testunit)