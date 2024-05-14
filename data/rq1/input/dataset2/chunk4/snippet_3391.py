#Source: https://stackoverflow.com/questions/47197960/attribute-error-using-python3x
sum = 0
num=""
while True:
    num=print("input no. :")
    if num.isdigit():
        sum=sum+int(num)
    else:
        break
print("sum is :",sum) 