#Source: https://stackoverflow.com/questions/44786828/typeerror-unbound-method-getdriver-must-be-called-with-driver-instance-as-f
from appium import webdriver

class Driver(object):

    def setUp(self):
        self.browser = 'iOS'
        self.getDriver(self.platform)

    def getDriver(self, platform):
        desired_caps = {}
        urlLink = "XXXXXXXX"
        if platform == 'android':
            self.driver = webdriver.Remote(urlLink, desired_caps)
        elif platform == 'iOS':
            desired_caps['platformName'] = 'iOS'
            desired_caps['platformVersion'] = '10.0'
            desired_caps['deviceName'] = 'XXXXXXX'
            print(desired_caps)
            self.driver = webdriver.Remote(urlLink, desired_caps)
        return self.driver

    def tearDown(self):
        self.driver.quit()