#Source: https://stackoverflow.com/questions/61816692/what-should-i-dotypeerror
import re

ffail = ""
with open("regex_sum_340933.txt", "r" , "UTF-8") as some_file:
    ffail = some_file.read()
count = 0

match = re.findall('[0-9]+', ffail)

for II in match:
    number = int(II)
    count = count + number
print(count)