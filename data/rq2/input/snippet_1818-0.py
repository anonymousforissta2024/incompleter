from collections import defaultdict

def hlper_fnc(test_str):
    cntr = defaultdict(int)
    for ele in test_str:
        cntr[ele] += 1
    return [val for val, chr in cntr.items() if chr % 2 != 0]
test_str = 'geekforgeeks is best for geeks'
print('The original string is : ' + str(test_str))
print('The Odd Frequency Characters are : ' + str(res))