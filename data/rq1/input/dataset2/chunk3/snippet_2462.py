#Source: https://stackoverflow.com/questions/43197848/python-regex-issue-involving-typeerror-expected-string-or-bytes-like-object
import re
original_file = open('jokes.txt', 'r+')
original_file.read()
original_file = re.sub("\d+\. ", "", original_file)