#Source: https://stackoverflow.com/questions/77393069/python-attributeerror-webdriver-object-has-no-attribute-launch-app
import pytest
import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

appium_server = "http://localhost:4723/wd/hub"

desired_cap = {

    # Emulator - Android
    "deviceName": "Nexus 4 API 30",
    "platformName": "Android",
    "platformVersion": "11.0",
    "udid": "emulator-5554",
    "appPackage": "com.epf.mip.uat",
    "appActivity": "com.epf.mip.uat.MainActivity"
}

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(desired_cap)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def appium_android_driver(request):
    print("Initializing Appium Android Driver")
    driver = webdriver.Remote(command_executor=appium_server, options=capabilities_options)

    yield driver

    if request.node.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Screen Before Error",  attachment_type=AttachmentType.PNG)

    driver.quit()