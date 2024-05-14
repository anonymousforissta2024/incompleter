def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))