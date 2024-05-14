def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
print(intersection(lst1, lst2))