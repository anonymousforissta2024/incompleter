#Source: https://stackoverflow.com/questions/73118754/filenotfounderror-in-unzipping-python-file
import os
import zipfile

directory = 'D:\\Python ds and alg by mostafa'
for file in os.listdir(directory):
    if file.endswith('.zip'):
        zipfile.ZipFile(file).extractall(directory)