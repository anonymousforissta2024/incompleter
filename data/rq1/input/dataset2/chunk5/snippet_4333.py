#Source: https://stackoverflow.com/questions/59409208/getting-a-typeerror-in-python
n= 5
def fact(n):
    if n== 0:
        return 1
    else:
        return (n*fact(n-1))

print(fact(n))