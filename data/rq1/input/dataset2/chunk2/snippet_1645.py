#Source: https://stackoverflow.com/questions/59633827/why-does-my-script-return-attributeerror-str-object-has-no-attribute-append
from observations.constants import PROJECTS_DB_ID
from datetime import datetime
from dateutil.relativedelta import relativedelta

def get(gs_client):
    #Sheet access
    sheet = gs_client.open_by_key(
        PROJECTS_DB_ID).worksheet('Finance')

    #Columns necessary
    projects = sheet.col_values(1)[2:]
    months = sheet.col_values(2)[2:]
    profit = sheet.col_values(11)[2:]
    revenue = sheet.col_values(6)[2:]
    last_modified = sheet.col_values(13)[2:]

    #Lists
    list_projects = []
    list_months = []
    list_profit = []
    list_revenue = []
    list_last_modified = []
    value = []

    #Gets each project
    for project in projects:
        list_projects.append(project)

    #Gets each month
    for month in months:
        list_months.append(month)

    #Gets each value of profit column
    for val in profit:
        list_profit.append(val.strip('$').replace(',',''))

    #Gets each value in revenue column
    for value in revenue:
        list_revenue.append(value.strip('$').replace(',',''))

    #Gets each date in last modified column
    for update in last_modified:
        list_last_modified.append(update)

    #Get profitability per project (profit divided by revenue)
    for x in range(len(projects)):
        value1 = float(list_profit[x])/float(list_revenue[x])
        value.append(value1)

    print(value)