from collections import defaultdict

def max_aggregate(st_data):
    temp = defaultdict(int)
    for name, marks in st_data:
        temp[name] += marks
    return max(temp.items(), key=lambda x: x[1])
print('Original list:')
print(students)
print('\nMaximum aggregate value of the said list of tuple pair:')
print(max_aggregate(students))