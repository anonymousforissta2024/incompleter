#Source: https://stackoverflow.com/questions/71448341/typeerror-object-of-type-numpy-int64-has-no-len-selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

df = pd.read_excel('data.xlsx')
print(df.iloc[1])

browser = webdriver.Chrome()
browser.get('https://my.web.site')

for i in df.index:
    entry = df.iloc[i]
    print(entry["CN"])
    print(entry["NIN"])
    CarteNational = browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div/input')
    CarteNational.send_keys(entry["CN"])
    NumeroIdentification = browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[5]/div/div/input')
    NumeroIdentification.send_keys(entry["NIN"])