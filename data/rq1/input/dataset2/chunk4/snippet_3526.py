#Source: https://stackoverflow.com/questions/70650986/attribute-error-while-scraping-gdelt-data
import gdelt
gd = gdelt.gdelt(version=1)
from statsmodels.tsa.api import VAR
import pandas as pd
import os
os.makedirs("data",exist_ok=True)
import datetime

cur_date = datetime.datetime(2022,1,10) - datetime.timedelta(days=10)
end_date = datetime.datetime(2022,1,10)

year     = cur_date.year
month    = str(cur_date.month)
day      = str(cur_date.day)

if cur_date.month < 10:
    month = "0" + month
if cur_date.day < 10:
    day = "0" + day  

gd.Search(['%s %s %s'%(year, month, day)],table='gkg',coverage=True, translation=False)