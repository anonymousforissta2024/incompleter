#Source: https://stackoverflow.com/questions/73640902/smartsheet-python-sdk-attributeerror-module-smartsheet-has-no-attribute-she
import smartsheet
import logging

TOKEN = '<<suppressed for security>>'

logging.getLogger('smartsheet').setLevel(logging.CRITICAL)
smart = smartsheet.Smartsheet(access_token=TOKEN)
action = smartsheet.Sheets.list_sheets(include_all=True)
print(action) # Just a placeholder to set a breakpoint