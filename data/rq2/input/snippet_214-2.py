import itertools

def interleave_multiple_lists(list1, list2, list3):
    result = list(itertools.chain(*zip(list1, list2, list3)))
    return result
list1 = [100, 200, 300, 400, 500, 600, 700]
list3 = [1, 2, 3, 4, 5, 6, 7]
print('Original list:')
print('list1:', list1)
print('list2:', list2)
print('list3:', list3)
print('\nInterleave multiple lists:')
print(interleave_multiple_lists(list1, list2, list3))