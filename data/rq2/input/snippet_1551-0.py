def get_max(sub):
    return max(sub)
print('The original list is : ' + str(test_list))
test_list.sort(key=get_max, reverse=True)
print('Sorted Tuples : ' + str(test_list))