#Source: https://stackoverflow.com/questions/75889310/attributeerror-testorders-object-has-no-attribute-token
import unittest
import HtmlTestRunner
from API_project.Tests.test_orders import TestOrders


class MyTestSuite(unittest.TestCase):
   
    def test_suite(self):
       
        test_to_run = unittest.TestSuite()
        test_to_run.addTests(
            [
            unittest.defaultTestLoader.loadTestsFromTestCase(TestOrders)
            ]
        )
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='TestProject',
            report_title = 'TestProjectUnitTesting'
        )
        runner.run(test_to_run)