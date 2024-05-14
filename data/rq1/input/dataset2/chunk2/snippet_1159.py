#Source: https://stackoverflow.com/questions/66814114/python-attributeerror-io-textiowrapper-object-has-no-attribute-append-er
for i in range(1, 100):
    f = open("IT TextBook Ques.txt", 'r')
    f2 = f.read()
    f1 = f"""{f2}
    Q.) \n"""
    f.close()
    f3 = open("IT TextBook Ques.txt", 'w')
    f3.write(f1)