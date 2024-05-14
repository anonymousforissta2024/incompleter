#Source: https://stackoverflow.com/questions/61876429/why-python-is-throwing-attribute-attribute-error
from utilities.teststatus import TestStatus as ts
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class testLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetup):
        self.lp = LoginPage(self.driver)
    @pytest.mark.order1
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        userIcon = self.lp.verifyLoginSuccessful()
        title = self.lp.verifyPageTitle()
        ts.markFinal(title,"Login not successful")
        assert userIcon == True