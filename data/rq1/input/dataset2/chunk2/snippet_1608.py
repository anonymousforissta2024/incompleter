#Source: https://stackoverflow.com/questions/74348377/python-selenium-by-raises-attributeerror-type-object-by-has-no-attribute-xpa
import socket
import httpcore
import re
import os
import json
import selenium
import httpx as web
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep