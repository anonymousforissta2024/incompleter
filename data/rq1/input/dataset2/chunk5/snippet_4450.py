#Source: https://stackoverflow.com/questions/44786828/typeerror-unbound-method-getdriver-must-be-called-with-driver-instance-as-f
import unittest
from core import Driver
import page

class testLoginOK(unittest.TestCase):

    def setUp(self):
        self.driver = Driver.getDriver('iOS')

    def test_login_error_message(self):

        main_page = page.MainPage(self.driver)
        main_page.click_Login_Button()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()