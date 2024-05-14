#Source: https://stackoverflow.com/questions/61825038/typeerror-list-indices-must-be-integers-or-slices-not-str-it-is-showing-in-if
lst = ['abc', 'Bcd', 'abf', 'bbc', 'Anv']

w = 0

for i in lst:

    if int(lst[i][0].isupper()) != 0:

        w += 1
print(w)