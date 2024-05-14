#Source: https://stackoverflow.com/questions/58334923/why-python-gives-typeerror-when-trying-to-call-a-function-that-read-text
#open the file and read it as a list
textlist = open('testfile.text', 'r').readlines()
#textlist = ['Build a machine\n', 'For the next generation']

#print the return_position as a lines
print(''.join(return_position(textlist, search_for=['a', 'b'])))