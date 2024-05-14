#Source: https://stackoverflow.com/questions/56572523/navernews-default-nameerror-name-navernews-is-not-defined
import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
sys.path.append('/NaverNews/Main/News/FirstNews')
sys.path.append('/NaverNews/Default/Default')

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

from FirstNews import *
from Default import *

import datetime
import random

random.seed(datetime.datetime.now())


class NaverNews:
    def __init__(self, NewsLists):
        self.FirstNewsSite = NewsLists
        # self.SecondNewsSite = NewsLists
        # self.ThirdNewsSite = NewsLists
        # self.FourthNewsSite = NewsLists
        # self.FifthNewsSite = NewsLists
        # self.RealTimeNews = NewsLists
        self.Default = NewsLists

    # @property
    # def NewsLists(self):
    #     return self.NewsLists

    # def SelectNums(self, new_NewsLists):
    def __call__(self):
        print("Please Select the News Site")
        MenuInput = input("Select The Menu")
        MenuList = []
        while 1:
            if MenuInput is 1:
                self.FirstNewsSite()
                MenuList.append(FirstNews)

            else:
                self.Default()
                MenuList.append(DefaultNews)