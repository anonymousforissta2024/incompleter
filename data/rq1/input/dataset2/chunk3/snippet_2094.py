#Source: https://stackoverflow.com/questions/16567713/fixed-python-nameerror-fixed-attributeerror-and-got-this
from random import *
from xml.dom import minidom
import parser
from parser import *
print("+---+ Roleplay Stat Reader +---+")
print("Load previous DAT file, or create new one (new/load file)")
IN=input()
splt = IN.split(' ')
if splt[0]=="new":
    xmlwrite(splt[1])
else:
    if len(splt[1])<2:
        print("err")
    else:
        xmlread(splt[1])
ex=input("Press ENTER to Exit...")