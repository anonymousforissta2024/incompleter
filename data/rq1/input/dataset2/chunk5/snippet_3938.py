#Source: https://stackoverflow.com/questions/51756290/python-functions-within-classes-nameerror-function-not-defined
from convert import CollateCSV
x = CollateCSV("./csv_files", "./file_list.csv", output=False)

print(x.list_files_to_reas())