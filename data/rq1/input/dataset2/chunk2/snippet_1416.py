#Source: https://stackoverflow.com/questions/37229359/money-and-typeerror-init-takes-from-1-to-2-positional-arguments-but-3-wer
from money import Money
class USD(Money):
    def __init__(self, amount='0'):
        super().__init__(amount=amount, currency='USD')
a = Money(0,'USD')
b = Money(-360,'USD')
a += b
print(a)
c = USD(0)
d = USD(-360)
c += d
print(c)