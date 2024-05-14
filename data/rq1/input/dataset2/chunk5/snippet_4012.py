#Source: https://stackoverflow.com/questions/46622020/attributeerror-nonetype-object-has-no-attribute-div
import sys
from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib.parse import quote

import os
import xlwt

import re  
import time
import random
import re, requests, csv
from bs4 import BeautifulSoup
from time import sleep

# CMD chcp 65001


def reviews_info(div):
    review_text = div.find("div", "review-content").div.text 
    review_stars = div.find("div", "i-stars i-stars--regular-1 rating-large").a.text
    return {
        "review_text" : review_text,
        "review_stars" : review_stars,
    }

base_url = "https://www.yelp.com/biz/founding-farmers-d-c-washington-2?start="
reviews = []
NUM_PAGES = 36

for page_num in range(1, NUM_PAGES + 20):
    print("souping page", page_num, ",", len(reviews), "data")
    url = base_url + str(page_num)
    soup = BeautifulSoup(requests.get(url).text, 'lxml') 

    for div in soup('div', 'review-content'):
        reviews.append(reviews_info(div))
    sleep(5)#############################################
    #  Save dict data
keys = reviews[0].keys()
with open('testtest.csv', 'w', encoding="utf-8") as f:
    dict_writer = csv.DictWriter(f, delimiter=',', lineterminator='\n', fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(reviews)