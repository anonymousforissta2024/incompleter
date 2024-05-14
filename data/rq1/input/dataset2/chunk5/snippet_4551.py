#Source: https://stackoverflow.com/questions/73066850/getting-attributeerror-nonetype-object-has-no-attribute-get-using-pytest
from self import self
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

def test_login(self, setup):
    self.driver = setup
    self.driver.get(self.baseURL)
    self.logger.info("URL iS loaded successfully")
    self.driver.maximize_window()

    self.lp = LoginPage(self.driver)

    self.lp.setUserName(self.username)
    self.logger.info("username   entered successfully")
    self.lp.setPassword(self.password)
    self.logger.info("password   entered successfully")
    self.lp.clickLogin()
    self.logger.info("clicked on login button")
    self.driver.close()