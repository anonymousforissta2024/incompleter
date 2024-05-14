#Source: https://stackoverflow.com/questions/55819002/attributeerror-classname-object-has-no-attribute-driver-on-appium-python
import unittest
from appium import webdriver
import time
import tracemalloc
tracemalloc.start()
from config import desired_caps
# self = webdriver
# self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


class BaseTest(unittest.TestCase):

    def test_testcase1(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_credentials(self):
        email = self.driver.find_element_by_xpath("proper Xpath")
        email.send_keys("Test")

        save = self.driver.find_element_by_link_text("Log In")
        save.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
    unittest.TextTestRunner(verbosity=3).run(suite)