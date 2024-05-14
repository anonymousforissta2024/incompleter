def count_digs(tup):
    return sum([len(str(ele)) for ele in tup])
print('The original list is : ' + str(test_list))
test_list.sort(key=count_digs)
print('Sorted tuples : ' + str(test_list))