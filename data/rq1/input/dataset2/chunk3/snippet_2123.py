#Source: https://stackoverflow.com/questions/62120840/why-am-i-getting-an-error-typeerror-system-takes-at-most-1-argument-3-given
import os

currentinfo = input("Enter username: ")

os.system('echo', "Username:", currentinfo, ">> info.txt")