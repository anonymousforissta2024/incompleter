str1 = 'sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
print('Original string: ', str1)
str_num = [i for i in str1.split(' ')]
numbers = sorted([int(x) for x in str_num if x.isdigit()])
print('Numbers in sorted form:')
for i in filter(lambda x: x > lenght, numbers):
    print(i, end=' ')