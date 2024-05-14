#Source: https://stackoverflow.com/questions/45996311/trying-to-sum-up-nested-lists-but-receive-error-typeerror-unsupported-operand-t
count = 0
lista=[[] for q in range(5)]
while count<len(lista):
    import random
    c=random.randrange(1,7,1)
    lista[count].append(c)
    count += 1

print(lista)
total=sum(lista)