#Source: https://stackoverflow.com/questions/35957085/python3-typeerror-list-indices-must-be-integers-or-slices-not-str
list = []

string = 'AAAABBBCCDAABBB'

i = 1

for i in string:
    list.append(i)

print(list)

for element in list:
    if list[element] == list[element-1]:
        list.remove(list[element])

print(list)