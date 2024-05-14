#Source: https://stackoverflow.com/questions/43858513/pytest-typeerror-init-got-an-unexpected-keyword-argument-browser
import pytest
from fixture.application import Application
__author__ = 'Max'

fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None:
        fixture = Application(browser=browser)
    else:
        if not fixture.is_valid:
            fixture = Application(browser=browser)
    fixture.session.ensure_login(username="somename", password="somepassword")
    return fixture

def pytest_addoption(parser):
    # hooks for browsers
    parser.addoption("--browser", action="store", default="chrome")