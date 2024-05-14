#Source: https://stackoverflow.com/questions/66085361/i-am-getting-an-error-when-i-try-to-use-a-setter-the-error-message-is-attribute
raise_amt = 1.04

def __init__(self, first, last, pay):
    self.first = first
    self.last = last

    self.pay = pay

def fullname(self):
    return '{} {}'.format(self.first, self.last)

@property
def email(self):
    return '{}.{}@email.com'.format(self.first, self.last)

@fullname.setter
def fullname(self,name):
    first,last=name.split(" ")
    self.first=first
    self.last=last