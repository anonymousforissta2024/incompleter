#Source: https://stackoverflow.com/questions/33380936/typeerror-function-object-is-not-subscriptable
def sumList(l):
    if l == []:
        return 0
    else:
        return sumList[1:] + [l[0]]
def main():
    l=[3,2,5,3]
    print(sumList(l))

main()