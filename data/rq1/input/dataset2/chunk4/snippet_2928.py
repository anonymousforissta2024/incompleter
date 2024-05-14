#Source: https://stackoverflow.com/questions/39957316/typeerror-init-takes-2-positional-arguments-but-3-were-given
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


myfile = [p.rstrip() for p in open('test.txt')]

for ip in myfile:

    driver = webdriver.Chrome('./lib/chromedriver.exe')
    driver.get("http://admin:password@" + ip)
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(By.XPATH, ".//*/tbody/tr/td/table/tbody/tr[2]/td[2]")
        )
    except TimeoutException:
        print(colored(ip + " except timeout error", "red"))

    else:
        print(colored(ip + " is OK", "green"))
    finally:
        driver.quit()