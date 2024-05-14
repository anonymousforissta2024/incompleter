#Source: https://stackoverflow.com/questions/55616035/typeerror-object-of-type-bytes-is-not-json-serializable-live-streaming-data
import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import json
import time
import random

# function for data_generation

def data_generation():
    surr_id = random.randint(1, 3)
    speed = random.randint(20, 200)
    date = datetime.today().strftime("%Y-%m-%d")
    time = datetime.now().isoformat()

    return [surr_id, speed, date, time]


if __name__ == '__main__':

    REST_API_URL = 'api_url'

    while True:
        data_raw = []
        for j in range(1):
            row = data_generation()
            data_raw.append(row)
            print("Raw data - ", data_raw)

        # set the header record
        HEADER = ["surr_id", "speed", "date", "time"]

        data_df = pd.DataFrame(data_raw, columns=HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        print("JSON dataset", data_json)

        # Post the data on the Power BI API
        try:
            req = requests.post(REST_API_URL, data=json.dumps(
                data_json), headers=HEADER, timeout=5)
            print("Data posted in Power BI API")
        except requests.exceptions.ConnectionError as e:
            req = "No response"
            print(req)

        time.sleep(3)