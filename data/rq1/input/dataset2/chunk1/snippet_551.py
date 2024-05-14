#Source: https://stackoverflow.com/questions/76444501/typeerror-init-got-multiple-values-for-argument-options
from time import time, sleep

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from args_parser import ArgsParser
from downloader import download_file

args = ArgsParser()


def print_if_verbose(val):
    if args.output_verbose:
        print(val)


WAITING_TIMEOUT = 180
chrome_options = Options()
driver_user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')
chrome_options.add_argument(f'user-agent={driver_user_agent}')
if not args.display_browser:
    chrome_options.add_argument('--headless')
try:
    driver = Chrome(ChromeDriverManager().install(), options=chrome_options)
except Exception as e:
    print(e)
    try:
        driver = Chrome("./chromedriver", options=chrome_options)
    except Exception:
        driver = Chrome("chromedriver.exe", options=chrome_options)