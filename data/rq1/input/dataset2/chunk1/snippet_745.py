#Source: https://stackoverflow.com/questions/8120019/typeerror-float-object-not-iterable
count=7
for i in count:
    num = float(input("Type a number, any number:"))
    if num == 0:
        zero+=1
    elif num > 0:
        positive+=1
    elif num < 0:
        negative+=1

print (positive)
print (negative)
print (zero)