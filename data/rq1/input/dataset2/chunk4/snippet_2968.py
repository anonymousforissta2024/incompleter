#Source: https://stackoverflow.com/questions/41175651/classes-in-python-attributeerror
class FindByXPATH_1():
    def __init__(self):
        self.driver_location = '/usr/local/bin/chromedriver'
        self.driver = webdriver.Chrome(self.driver_location)
        self.driver.get('https://letskodeit.teachable.com/p/practice')

from basics.xpath_1 import FindByXPATH_1
import basics #the classes are in two different python files

class FindByXpath_2(FindByXPATH_1):
    def __init__(self):
        FindByXPATH_1.__init__(self)

    def find_by_starts_with(self):
        starting_with = FindByXPATH_1.driver.find_elements(By. XPATH, 
        '//div[@class="view-school"]//h3[starts-with(@)class, "subtitle"]')
        print(len(starting_with))

test = FindByXPATH_2()
test.find_by_starts_with()