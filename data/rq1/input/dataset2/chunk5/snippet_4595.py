#Source: https://stackoverflow.com/questions/68551441/how-do-i-fix-attributeerror-list-object-has-no-attribute-strip
fin = open('gift1.in','r')
p= fin.readline().split(",")
np = int(p.strip())
dictOfMoney = { fin.readline().strip() : 0 for i in range(np) }

while(True):
    giver = fin.readline().strip()
    if(giver==""):
        break
    amount, divided = map(int, fin.readline().strip().split())
    receivers = [fin.readline().strip() for i in range(divided)]

    try:
        quotient, remainder = divmod(amount,divided)
    except:
        quotient = remainder = 0

    for receiver in receivers:
        dictOfMoney[receiver] += quotient
    dictOfMoney[giver] += -amount + remainder

with open('gift1.out','w') as fout:
    for name, money in dictOfMoney.items():
        fout.write(f"{name} {money}\n")