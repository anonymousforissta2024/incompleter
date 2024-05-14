#Source: https://stackoverflow.com/questions/45252305/attributeerror-module-sys-has-no-attribute-setdefaultencoding
#py3.6, windows10   
import time
from selenium import webdriver
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')