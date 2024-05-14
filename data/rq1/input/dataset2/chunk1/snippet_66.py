#Source: https://stackoverflow.com/questions/71946233/typeerror-textiowrapper-seek-takes-no-keyword-arguments
with open("t.txt",'a+') as f:
    f.seek(0,)
    print(f.readlines())
    f.seek(0,whence=0)
    f.write("12\n23\n32")