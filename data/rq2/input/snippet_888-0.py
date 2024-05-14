str1 = 'sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
print('Original string: ', str1)
str_num = [i for i in str1.split(' ')]
lenght = len(str_num)
print('Numbers in sorted form:')
for i in filter(lambda x: x > lenght, numbers):
    print(i, end=' ')