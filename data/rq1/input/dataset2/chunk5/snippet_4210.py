#Source: https://stackoverflow.com/questions/56447938/typeerror-get-token-missing-1-required-positional-argument-bs4
import requests
from bs4 import BeautifulSoup

class checker_start(object):
    def get_token(self, bs4):
        data = requests.get("https://login.live.com")
        soup = bs4.BeautifulSoup(data.text, 'lxml')

        token_1 = soup.find("input", {"value": "flowToken"})["value"]
        return token_1


print(checker_start().get_token())