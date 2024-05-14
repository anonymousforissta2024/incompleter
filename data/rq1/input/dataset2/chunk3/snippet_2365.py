#Source: https://stackoverflow.com/questions/63430336/python-bokeh-pandas-attributeerror-unexpected-attribute-responsive-to-fig
from bokeh.plotting import Figure, output_file, show
import pandas

file="adbe.csv"

df=pandas.read_csv(file, parse_dates=["Date"])

p=figure(width=500, height=500, x_axis_type="datetime", responsive = True)

p.line(df["Date"],df["Close"],color="Orange", alpha=0.5)

output_file("Time_Series.html")
show(p)