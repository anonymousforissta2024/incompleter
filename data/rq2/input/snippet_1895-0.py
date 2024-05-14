import numpy
List = [1, 2, 3, 4, 5]
Array = numpy.array(List)
print('Array:\n', Array)
file = open('file1.txt', 'w+')
file.write(content)
file.close()
file = open('file1.txt', 'r')
content = file.read()
print('\nContent in file1.txt:\n', content)
file.close()