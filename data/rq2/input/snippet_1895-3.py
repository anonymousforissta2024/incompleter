import numpy
Array = numpy.array(List)
print('Array:\n', Array)
file = open('file1.txt', 'w+')
content = str(Array)
file.write(content)
file.close()
file = open('file1.txt', 'r')
content = file.read()
print('\nContent in file1.txt:\n', content)
file.close()