#Source: https://stackoverflow.com/questions/77393069/python-attributeerror-webdriver-object-has-no-attribute-launch-app
@pytest.mark.usefixtures("appium_android_driver")
class TestSuite_EPF_Android_App:

    def test_initialAppLaunch(self, appium_android_driver):

        launching_iAkaun_Application(self.driver)