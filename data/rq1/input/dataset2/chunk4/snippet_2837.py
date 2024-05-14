#Source: https://stackoverflow.com/questions/66296031/why-driver-find-elements-by-class-name-click-results-in-attributeerror
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://website.com/signup')
time.sleep(1)

button = driver.find_elements_by_class_name("continue")
button.click()
time.sleep(1)