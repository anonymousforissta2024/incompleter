#Source: https://stackoverflow.com/questions/76550506/typeerror-webdriver-init-got-an-unexpected-keyword-argument-executable-p
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=option)

driver.get('https://www.google.com/')