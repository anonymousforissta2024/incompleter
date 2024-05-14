#Source: https://stackoverflow.com/questions/59078817/keep-on-getting-an-attributeerror-and-not-sure-why
def gcd(n, d):
        if n==0 or d==0:
            return 1
        while(n != d):
            if(n > d):
                n = n - d
            else:
                d = d - n
        return n

class Fraction:
    def __init__(self, n, d):
        self.num = int(n / gcd(abs(n), abs(d)))
        self.denom = int(d / gcd(abs(n), abs(d)))
        if self.denom < 0:
            self.denom = abs(self.denom)
            self.num = -1 * self.num
        elif self.denom == 0:
            raise ZeroDivisionError
    def __str__(self):
        if type(self) is tuple:
            if self[1] < 0:
                return '%s/%s' %(self[0], -1*self[1])
            else:
                return '%s/%s' %(self[0], self[1])
        elif self.denom == 1:
            return str(self.num)
        else:
            return '%s/%s' %(self.num, self.denom)

    def __add__(self, other):
        return self.num*other.denom + self.denom*other.num, self.denom*other.denom

    def __sub__(self, other):
        return self.num*other.denom - self.denom*other.num, self.denom*other.denom

    def __mul__(self, other):
        return self.num*other.num, self.denom*other.denom

    def __div__(self, other):
        return self.num*other.denom, self.denom*other.num

    def __eq__(self, other):
        if self.num == other.num and self.denom == other.denom:
            return "Equal"
        else:
            return "Not Equal"


f1 = Fraction(2, 4)
f2 = Fraction(4, 20)
add = Fraction.__add__(f1, f2)
sub = Fraction.__sub__(f1, f2)
eq = Fraction.__eq__(f1, f2)
mul = Fraction.__mul__(f1, f2)
div = Fraction.__div__(f1, f2)
print("Fraction one: "+str(Fraction.__str__(f1))+"\n"+"Second Fraction: "+str(Fraction.__str__(f2))+"\n"+"Add: "+str(Fraction.__str__(add))+"\n"+"Subtract: "+str(Fraction.__str__(sub))+"\n"+"Multiply: "+str(Fraction.__str__(mul))+"\n"+"Divide: "+str(Fraction.__str__(div))+Fraction.__str__(eq))