#Source: https://stackoverflow.com/questions/51770485/typeerror-object-of-type-dataframe-is-not-json-serializable
import dash
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import psycopg2 as pg2
import datetime

conn = pg2.connect(database='X',user='X',password=secret)

cur = conn.cursor()

cur.execute("SELECT * FROM times;")
a = cur.fetchall()
str(a)


df = pd.DataFrame([[ij for ij in i] for i in a])
df.to_json()
df.rename(columns={0: "Serial Number", 1: "Status", 2: "Date", 3: "Time", 4: "Number"}, inplace=True);

x = df["Date"]
data = [go.Scatter(
            x=x,
            y=df["Status"])]

layout = go.Layout(title="Server Data Visualization",
                   xaxis = dict(
                   range = [df.head(1),
                            df.tail(1)]),
                    yaxis=dict(title = "Status"))

fig = go.Figure(data = data, layout = layout)
py.plot(fig)