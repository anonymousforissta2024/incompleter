#Source: https://stackoverflow.com/questions/62907338/filenotfounderror-with-selenium-python-3-8
from time import sleep
from selenium import webdriver
driver = webdriver.Firefox(executable_path='/opt/geckoDriver/geckodriver.exe')
driver.get('https://instagram.com/')
sleep(5)
driver.close()