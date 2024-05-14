#Source: https://stackoverflow.com/questions/74953823/python-filenotfounderror
import json 

def print_name():
    with open(file=r"test.json",mode='r') as json_file :
        py_dict = json.load(json_file)
    print(py_dict["name"])

print_name()