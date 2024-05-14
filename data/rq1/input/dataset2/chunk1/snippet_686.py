#Source: https://stackoverflow.com/questions/60699518/attributeerror-lifoqueue-object-has-no-attribute-put-selenium-webdriver
import selenium
from selenium import webdriver

options = webdriver.chrome.options.Options()

options.add_argument('--no-sandbox') 
options.add_argument('--disable-dev-shm-usage')

chromedriver = '/usr/bin/chromedriver'

print('test0') #is being printed

driver = webdriver.Chrome('/usr/bin/chromedriver',options=options)

print('test') #not being printed

driver.get('http:google.com')