color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', 'w') as myfile:
    for c in color:
        myfile.write('%s\n' % c)
print(content.read())