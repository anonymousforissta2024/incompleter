#Source: https://stackoverflow.com/questions/68968383/attributeerror-while-attempting-to-grab-table-from-a-website-in-python-bs
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome('C://Python38/chromedriver')
browser.get("https://poocoin.app/rugcheck/0xe56842ed550ff2794f010738554db45e60730371/top-holders")
url = "https://poocoin.app/rugcheck/0xe56842ed550ff2794f010738554db45e60730371/top-holders"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
t = soup.find('table', class_='table table-bordered table-condensed text-small')
trs = t.find('tbody').find_all('tr')
for tr in trs[:10]:
    print(list(tr.stripped_strings))
browser.quit()