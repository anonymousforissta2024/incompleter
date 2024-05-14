#Source: https://stackoverflow.com/questions/59117601/getting-typeerror-not-all-arguments-converted-during-string-formatting
def reverse(num):
    r=0
    while(num!=0):
        r=(r*10)+(num%10)
        num //= 10
    return r

num=input("Enter a number: ")
n=reverse(num)
numOdd=[]
numEven=[]
c=1
while(n!=0):
    if (c%2==0):
        numEven.append(n%10)
    else:
        numOdd.append(n%10)
    n//= 10
    c += 1
sortedEven=True
sortedOdd=True
for i in range(len(numOdd)-1):
    if(numOdd[i]>numOdd[i+1]):
        sortedOdd=False
for i in range(len(numEven)-1):
    if(numEven[i]<numEven[i+1]):
        sortedEven=False

if(sortedOdd==True and sortedEven==True):
    print ("True")
else:
    print ("False")