def interleave_multiple_lists(list1, list2, list3):
    result = [el for pair in zip(list1, list2, list3) for el in pair]
    return result
list2 = [10, 20, 30, 40, 50, 60, 70]
list3 = [100, 200, 300, 400, 500, 600, 700]
print('Original list:')
print('list1:', list1)
print('list2:', list2)
print('list3:', list3)
print('\nInterleave multiple lists:')
print(interleave_multiple_lists(list1, list2, list3))