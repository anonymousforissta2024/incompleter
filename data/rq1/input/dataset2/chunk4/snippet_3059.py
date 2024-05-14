#Source: https://stackoverflow.com/questions/64841890/dataframe-to-google-spreadsheet-typeerror-dataframe-objects-are-mutable-th
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import gspread
from googleapiclient import discovery

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('SpreadsheetName').sheet1

sheets_service = discovery.build('sheets','v4',credentials=credentials)
sheets = sheets_service.spreadsheets()
spreadsheet_id = '************************'


def df_to_sheet(df):
    df_columns = [np.array(df.columns)]
    df_values = df.values.tolist()
    df_to_sheet = np.concatenate((df_columns, df_values)).tolist()
    return df_to_sheet

data = [
    {
        "title": "Unique URL",
        "df": pd.DataFrame({})
    }
]
update_body = {
        "valueInputOption": "RAW",
        "data": list(map(lambda d: {"range": d.get("title"), "values": df_to_sheet(d.get(df))}, data))
    }
sheets.values().batchUpdate(spreadsheetId=spreadsheet_id, body=update_body).execute()