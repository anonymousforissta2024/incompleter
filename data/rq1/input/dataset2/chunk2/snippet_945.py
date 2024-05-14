#Source: https://stackoverflow.com/questions/50799363/when-i-run-my-test-suite-i-am-getting-a-typeerror-i-am-not-able-to-understand-wh
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from tests.Home import category_test

example_tests = TestLoader().loadTestsFromTestCase(category_test)
suite = TestSuite(example_tests)
runner = HTMLTestRunner(output='example_suite', template='path/to/template', report_title='My Report')
runner.run(suite)