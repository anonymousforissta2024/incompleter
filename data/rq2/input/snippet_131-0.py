def list_difference(l1, l2):
    result = list(l1)
    for el in l2:
        result.remove(el)
    return result
l2 = [1, 1, 2, 4, 5, 6]
print('Original lists:')
print(l1)
print(l2)
print('\nDifference between two said list including duplicate elements):')
print(list_difference(l1, l2))