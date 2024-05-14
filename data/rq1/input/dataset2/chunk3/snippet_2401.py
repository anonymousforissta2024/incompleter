#Source: https://stackoverflow.com/questions/47870000/typeerror-export-users-xls-missing-1-required-positional-argument-request
url(r'^users/print$',views.export_users_xls(),name="Exceldata"),