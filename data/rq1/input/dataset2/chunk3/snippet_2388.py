#Source: https://stackoverflow.com/questions/44598427/open-a-html-file-inside-a-zip-file-python-3-6-typeerror-zipfile-object-is-n
import zipfile


file = zipfile.ZipFile("John.zip", "r")


with file('John.zip') as myzip:
    with myzip.open("news.html") as myfile:
        print(myfile.read())