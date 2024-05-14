test_list = [{'Nikhil': 17, 'Akash': 18, 'Akshat': 20}, {'Nikhil': 21, 'Akash': 30, 'Akshat': 10}, {'Nikhil': 31, 'Akash': 12, 'Akshat': 19}]
print('The original list is : ' + str(test_list))
for idx, sub in enumerate(test_list, start=0):
    if idx == 0:
        res.append(list(sub.keys()))
        res.append(list(sub.values()))
    else:
        res.append(list(sub.values()))
print('The converted list : ' + str(res))