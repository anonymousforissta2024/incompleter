#Source: https://stackoverflow.com/questions/59871383/why-typeerror-unhashable-type-list-when-calling-function
a = [5,5,6,7,7,7]
b = set(a)
def test(lst):
    if lst in b:
        return 1
    else:
        return 0
print(test(a))  #this gives me error list unhashable  
print(test,a)   #how this is working
for i in  filter(test, a):
    print(i,end=" ")