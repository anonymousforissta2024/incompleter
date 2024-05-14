from collections import Counter
test_list = ['geeksforgeeks is best for geeks']
print('The original list : ' + str(test_list))
res = {key: val for key, val in dict(Counter(''.join(test_list))).items() if key in chr_list}
print('Specific Characters Frequencies : ' + str(res))