#Source: https://stackoverflow.com/questions/50895680/typeerror-firefoxwebelement-object-is-not-iterable
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

test_url = 'https://www.airbnb.jp/s/%E6%97%A5%E6%9C%AC%E6%B2%96%E7%B8%84%E7%9C%8C/homes?refinement_paths%5B%5D=%2Fhomes&query=%E6%97%A5%E6%9C%AC%E6%B2%96%E7%B8%84%E7%9C%8C&price_min=15000&allow_override%5B%5D=&checkin=2018-07-07&checkout=2018-07-08&place_id=ChIJ51ur7mJw9TQR79H9hnJhuzU&s_tag=z4scstF7'

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts)
driver.get(test_url)
driver.implicitly_wait(30)

for links in driver.find_element_by_xpath('//div[contains(@id, "listing-")]//a[contains(@href, "rooms")]'):
    listing_url = links.get_attribute('href')
    print(listing_url)

driver.quit()