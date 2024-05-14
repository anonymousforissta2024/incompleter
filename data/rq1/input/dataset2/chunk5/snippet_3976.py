#Source: https://stackoverflow.com/questions/59993853/why-does-nameerror-name-not-defined-occur-when-executing-python-file-external
import os
import pandas as pd
from multiprocessing import Pool
from datetime import timedelta, date
from external_functions import get_api_item #separate .py file with a function

def date_range(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2020, 1, 29)
end_date = date(2020, 1, 30)
date_list = []

for single_date in date_range(start_date, end_date):
    date_list.append(single_date.strftime('%Y-%m-%d'))

if __name__ == '__main__':
    global results
    p = Pool(20)
    results = p.map(get_api_item, date_list)
    p.terminate()
    p.join()

result = pd.concat(results)