#Source: https://stackoverflow.com/questions/43578116/dictionary-error-typeerror-str-object-does-not-support-item-assignment
import os

f = open("save")
forbidden = f.readline()
forbiddens = f.readline()
dictionary = f.readline()
stop = 0
global arguments
print("phonebook os by me")

def write():
    global forbidden
    global forbiddens
    global dictionary
    f = open("save")
    f.write(forbidden and '\n' and forbiddens and '\n' and dictionary)
    f.close()

def add_cc():
    global forbidden
    global dictionary
    global arguments
    name = arguments[1]
    number = int(arguments[2])
    if name in forbidden:
        print("403: forbidden!")
    elif name in dictionary:
        print("406: Not acceptable! This item is already in the dictionary!")
    else:
        dictionary[name] = number
    write()
    start()

def del_cc():
    global arguments
    global dictionary
    name = arguments[1]
    del dictionary[name]
    write()
    start()

def get_cc():
    global arguments
    global forbidden
    global dictionary
    name = arguments[1]
    if name in dictionary:
        print(dictionary[name])
    elif name in forbidden:
        print("403: Forbidden!")
    else:
        print("404: Item not Found.")
    start()