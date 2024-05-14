#Source: https://stackoverflow.com/questions/50799363/when-i-run-my-test-suite-i-am-getting-a-typeerror-i-am-not-able-to-understand-wh
from pages.Home.category_page import CategoryPage
from utilites.testStatus import TestStatus
import pytest
import unittest
import time

@pytest.mark.usefixture("oneTimeSetUp","setUp")
class CategoryTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.ca = CategoryPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_Announcements_link_WAF001(self):
        result = self.ca.find_announcements_link()
        self.ts.markFinal("Announcements link", result,"To find announcements link")
        time.sleep(2)

    @pytest.mark.run(order=2)
    def test_FirstLinkInAnnouncements_WAF002(self):
        result=self.ca.find_first_announcement_link()
        self.ts.markFinal("Latest link in announcements",result,"To click on latest announcements link")
        time.sleep(2)

    @pytest.mark.run(order=3)
    def test_Products_Link_WAF003(self):
        result=self.ca.find_products()
        self.ts.markFinal("Products link",result,"To find products link")
        time.sleep(2)

    @pytest.mark.run(order=4)
    def test_FirstLinkInProducts_WAF004(self):
        result=self.ca.find_first_products_link()
        self.ts.markFinal("Latest link in products",result,"To click on latest products link")
        time.sleep(2)