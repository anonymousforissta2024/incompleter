#Source: https://stackoverflow.com/questions/76424247/typeerror-selenium-webdriver-remote-webdriver-webdriver-find-element-argument
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        checkoutPage = CheckoutPage(self.driver)
        elements = checkoutPage.getcardTitles()
        confirmPage = ConfirmPage(self.driver)
        i = -1
        for ele in elements:
            i = i + 1
            if ele.text == "Blackberry":
                checkoutPage.getcardFooter()[i].click()
        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        checkoutPage.checkoutButton().click()
        time.sleep(5)
        # self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        confirmPage.checkoutConfirm().click()
        self.driver.find_element(By.ID, "country").send_keys("Bangla")
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='suggestions'] ul li a")))
        self.driver.find_element(By.CSS_SELECTOR, "div[class='suggestions'] ul li a").click()
        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        success = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        assert "Success! Thank you!" in success