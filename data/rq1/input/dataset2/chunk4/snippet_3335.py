#Source: https://stackoverflow.com/questions/33703951/getting-typeerror-object-of-type-builtin-function-or-method-has-no-len
def CheckLength(num):
    if len(num)>=13 and len(num)<=16:
        return True
    else:
        return False
def CheckType(num):
    if num[0]=='4':
        return 'Visa'
    elif num[0]=='5':
        return 'MasterCard'
    elif num[0]=='6':
        return 'Discover'
    elif num[0:1]=='37':
        return 'American Express'
    else:
        return 'Invalid Entry'
def Step1(num):
    total=0
    length=len(num)
    for i in range(length-1,-2,-2):
        double=int(num[i]*2)
        if double>9:
            double=double[0]+double[1]
            total+=double
        else:
            total+=double
        return total        
def Step2(num):
    total=0
    length=len(num)
    for i in range(length-1,-1,-2):
        total+=i
    return total
def Step3(num):
    total=Step1(num)+Step2(num)
    if total%10==0:
        return True
    else:
        return False
def main():
    inFile=open('pa7.cards','r')
    cardNum=inFile.readline().strip()
    while cardNum!='99999':
        validLength=CheckLength(cardNum)
        validType=CheckType(cardNum)
        if validLength==True and validType==True:
            print(cardNum,"valid")
        else:
            print(cardNum,"invalid")
        cardNum=inFile.readline().strip
    inFile.close()
main()    