from collections import Counter
print('The original list : ' + str(test_list))
chr_list = ['e', 'b', 'g']
res = {key: val for key, val in dict(Counter(''.join(test_list))).items() if key in chr_list}
print('Specific Characters Frequencies : ' + str(res))