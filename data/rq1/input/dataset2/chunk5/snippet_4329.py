#Source: https://stackoverflow.com/questions/41705972/python-3x-typeerror-list-indices-must-be-integers-or-slices-not-str
list_1 = [the, cat, sat, on, mat]
list_2 = [1, 2, 3, 4, 1, 5]
list_3 = []

for i in list_2:
  list_3.append(list_1[i])