test_list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
print('The original list : ' + str(test_list))
for word in test_list[:]:
    if word.endswith(suff):
        test_list.remove(word)
print('List after removal of suffix elements : ' + str(test_list))