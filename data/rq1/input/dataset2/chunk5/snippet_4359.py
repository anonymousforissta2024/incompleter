#Source: https://stackoverflow.com/questions/44786828/typeerror-unbound-method-getdriver-must-be-called-with-driver-instance-as-f
from locators import Locators

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def click_Login_Button(self):
        element = self.driver.find_element(*Locators.setLocators().ACEPTAR_LOGIN_BTN)
        element.click()