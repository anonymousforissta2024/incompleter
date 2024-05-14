#Source: https://stackoverflow.com/questions/55146969/filenotfounderror-long-file-path-python-filepath-longer-than-255-characters
import os, sys
import argparse
import win32api
import win32con
import win32security
from os import walk

parser = argparse.ArgumentParser(
    description='Migration Script',
)

parser.add_argument('-p', '--home_path',  required = True, help='Home Drive Path')

args = vars(parser.parse_args())

if args['home_path']:
    pass
else:
    print("Usage : script.py -p <path>")
    print("-p <directory path>/")
    sys.exit()

dst = (args['home_path'] + '/' + 'long_file_path_dir')

for dirname, dirnames, filenames in os.walk(args['home_path']):
    for filename in filenames:
        file_path = (dirname + '/' + filename)
        path_len = len(file_path)
        if(path_len > 255):
            #short_path = win32api.GetShortPathName(file_path)
            copyfile(file_path, dst, follow_symlinks=True)