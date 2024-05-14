#Source: https://stackoverflow.com/questions/73433600/selenium-python-typeerror-str-object-is-not-callable-whenever-trying-to-prin
from cgitb import text
from http import server
from re import search
import selenium
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://t.me/s/klfjezlkjfzlek")
test = driver.find_element(By.XPATH("//html//body//main//div//section//div//div//div//div[@class='tgme_widget_message_text js-message_text before_footer'][last()]"))
source_code = test.text
print(source_code)