#Source: https://stackoverflow.com/questions/41153215/sum-columns-in-2-d-array-typeerror-list-indices-must-be-integers-or-slices-no
array = [[3, 5, 7, 9]
        [2, 7, 3, 5],
        [1, 2, 6, 3],
        [6, 9, 5, 3]]

column_sum = []
total = 0
i = 0
for row in aList:
    total = total + row[i]
    column_sum.append(total)
    total = 0
    i = i + 1
print(column_sum)