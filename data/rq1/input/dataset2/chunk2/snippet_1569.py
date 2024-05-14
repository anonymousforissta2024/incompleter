#Source: https://stackoverflow.com/questions/57877513/attributeerror-tuple-object-has-no-attribute-replace-for-brackets
import os
os.chdir("/home/ubuntu/Desktop")
nfiles=os.listdir(os.getcwd())
new_files = [nfile for nfile in nfiles if nfile[-4:].lower()=='.txt']

for file in new_files:

    name = file
    name=name.replace=(")","")
    name=name.replace=(",","_")
    print(name)