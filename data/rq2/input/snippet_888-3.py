print('Original string: ', str1)
str_num = [i for i in str1.split(' ')]
lenght = len(str_num)
numbers = sorted([int(x) for x in str_num if x.isdigit()])
print('Numbers in sorted form:')
for i in filter(lambda x: x > lenght, numbers):
    print(i, end=' ')