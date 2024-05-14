import numpy as np
from ast import literal_eval
name_list = '{\n   "column0": {"First_Name": "Akash",\n   "Second_Name": "kumar", "Interest": "Coding"},\n                  \n   "column1": {"First_Name": "Ayush",\n   "Second_Name": "Sharma", "Interest": "Cricket"},\n     \n   "column2": {"First_Name": "Diksha",\n   "Second_Name": "Sharma","Interest": "Reading"},\n     \n   "column3": {"First_Name":" Priyanka",\n   "Second_Name": "Kumari", "Interest": "Dancing"}\n     \n  }'
print('Type of name_list created:\n', type(name_list))
t = literal_eval(name_list)
print('\nPrinting the original Name_list dictionary:\n', t)
print('Type of original dictionary:\n', type(t))
print('\nConverted ndarray from the Original dictionary:\n', result_nparra)
print('Type:\n', type(result_nparra))