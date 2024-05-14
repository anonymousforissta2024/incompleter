#Source: https://stackoverflow.com/questions/40554805/attributeerror-module-selenium-webdriver-has-no-attribute-firefox
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)