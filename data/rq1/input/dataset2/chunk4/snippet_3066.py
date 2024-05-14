#Source: https://stackoverflow.com/questions/76424247/typeerror-selenium-webdriver-remote-webdriver-webdriver-find-element-argument
from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkoutButton = (By.CSS_SELECTOR, "nav-link btn btn-primary")

    def getcardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitles)

    def getcardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)