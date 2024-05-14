#Source: https://stackoverflow.com/questions/60706749/getting-filenotfounderror-when-calling-python-coded-file-from-robot-framework
# setup.py

from robot.libraries.BuiltIn import BuiltIn
import xlrd


def get_variables(env):
    file_location = "values.xlsx"
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_name(env)
    print("Env : " + sheet.name)
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
    print(data)
    BuiltIn().log_to_console(data)
    return data