#Source: https://stackoverflow.com/questions/50346338/typeerror-write-points-got-multiple-values-for-argument-time-precision-to-i
from influxdb import InfluxDBClient
from influxdb import DataFrameClient
import pandas as pd
Host_IP = 'XXXXXXXX'
Port = XXXX
User = 'XXXX'
Password = 'XXX'
DB_Name = 'XXXX'
client = InfluxDBClient(Host_IP, Port, User, Password,DB_Name)
df = pd.DataFrame(data=list(range(30)),index=pd.date_range(start='2014-11-16',periods=30, freq='H'))
client.write_points(df, 'demo',{'k1': 'v1', 'k2': 'v2'}, time_precision=None, protocol='json')