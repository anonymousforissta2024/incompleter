#Source: https://stackoverflow.com/questions/69707447/attributeerror-list-object-has-no-attribute-write
def modifytext2():
    file1 = open('data_user1.txt' , 'r') #read from txt file
    f = file1.readlines()
    g = [i.replace('@','---') for i in f]
    
    print(g)
    file1.close()

modifytext2()