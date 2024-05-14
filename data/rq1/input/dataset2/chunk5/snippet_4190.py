#Source: https://stackoverflow.com/questions/33321732/python-rookie-prob-type-error-mistake
a=input("Enter your first number")
b=input("And your second one")
if a>b:
    if a%b==0:
        print("YES")
    else:
        print("NO")
else:
    if b%a==0:
        print("YES")
    else :
        print ("NO")