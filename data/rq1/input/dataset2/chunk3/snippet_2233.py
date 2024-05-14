#Source: https://stackoverflow.com/questions/71626403/dash-plotly-error-typeerror-object-of-type-dataframe-is-not-json-serializable
import dash_bootstrap_components as dbc
from dash import dcc
import dash_html_components as html
from dash import dash_table
import pandas as pd
import numpy as np

def getData():
    return preprocess()

def back_to_df(dictio):
    return pd.DataFrame.from_dict(dictio)

tblcols  =[{"name": i, "id": i} for i in back_to_df(getData()).columns]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
body = html.Div([
    html.H1("Live rates")
    , dbc.Row([
            dbc.Col(html.Div([dcc.Interval('graph-update', interval = 80, n_intervals = 0),
      dash_table.DataTable(
          id = 'table',
          data = getData(),
          columns=tblcols,
          page_size= 10,
          style_table={'overflowX': 'auto'},
      )]),width=3)
            ])
        ])
app.layout = html.Div([body])

@app.callback(
        dash.dependencies.Output('table','data'),
        [dash.dependencies.Input('graph-update', 'n_intervals')])
def updateTable(n):
     return getData()

if __name__ == "__main__":
  app.run_server(debug = False, port = 8010)