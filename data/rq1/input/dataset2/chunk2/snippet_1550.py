#Source: https://stackoverflow.com/questions/48946999/django-and-selenium-typeerror-setupclass-missing-1-required-positional-argume
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class LevelListViewTest(StaticLiveServerTestCase):

    @staticmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @staticmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        cls.selenium.tearDownClass()

    def test_level_is_in_admin_panel(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/?next=/admin/'))