#Source: https://stackoverflow.com/questions/68987451/attributeerror-str-object-has-no-attribute-request
import os
from googleapiclient import discovery
import pandas as pd

credential = 'reference/config.json'
api_name = 'sheets'
api_version = 'v4'
scope = ['https://www.googleapis.com/auth/spreadsheets']

service = discovery.build('sheets','v4',credentials=credential)

sheet_id = [sheet_id]
ranges = 'Sheet1!D5:J36'

sheet = service.spreadsheets()
request = sheet.values().get(spreadsheetId=sheet_id, range=ranges, majorDimension='ROWS')
response = request.execute()