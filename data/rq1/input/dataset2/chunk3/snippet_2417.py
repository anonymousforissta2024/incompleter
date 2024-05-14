#Source: https://stackoverflow.com/questions/71764549/python-error-attributeerror-enter-using-selenium
from asyncio import selector_events
from lib2to3.pgen2 import driver
import booking.constants as const
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Booking:
    def __init__(self, teardown = False):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(const.BASE_URL)
        self.driver.teardown = teardown
        self.driver.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.driver.teardown:
            self.driver.quit()

    def cookies(self):
        self.driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

    def select_place_to_go(self):
        self.driver.find_element(By.ID, "ss").click()