#Source: https://stackoverflow.com/questions/73591649/how-to-fix-nameerror-when-i-call-a-function-from-another-file
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver.v2 as uc

if __name__ == '__main__':

        options = uc.ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        # e.g. Chrome path in Mac =/Users/x/Library/xx/Chrome/Default/
        # options.add_argument( "--user-data-dir=<Your chrome profile>")
        driver = uc.Chrome(options=options)
        url='https://accounts.google.com/servicelogin'
        driver.get(url)
        # add email
        driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(gmail_uid)
        driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
       
        driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(gmail_pwd)
        driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
       

        def my_custom_function(url):

                get_url = driver.get(url)

                return get_url