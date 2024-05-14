#Source: https://stackoverflow.com/questions/28354945/why-am-i-getting-typeerror-int-object-not-iterable
amx = []

def validamount(amount, limit):
    if amount >= limit:
        return amount
    else:
        return 0

def main():
    for i in 10:
        amx.append(int(input()))
    for i in 10:
        print(validamount(amx[i], 5))

main()