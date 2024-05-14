#Source: https://stackoverflow.com/questions/73700748/nameerror-name-check-balance-is-not-defined
class tree():
    def __init__(self,a=None,lc=None,rc=None):
        self.label=a
        self.lt=lc
        self.rt=rc
        if a is not None:
            if lc is None:
                self.lt=tree()
            if rc is None:
                self.rt=tree()

    def getLabel(self):
        return self.label

    def isEmpty(self):
        return self.label is None

    def isLeaf(self):
        return (self.lt.isEmpty() and self.rt.isEmpty())

    def getLc(self):
        return self.lt

    def getRc(self):
        return self.rt
    
    def check_balance(t):
        if t.isLeaf() or t.isEmpty():
            return True
        if t.getLc().isEmpty() or t.getRc().isEmpty():
            return False
        return check_balance(t.getLc()) and check_balance(t.getRc())

a = tree(1, tree(2, tree(7), tree(8)), tree(3, tree(7), tree()))
print(check_balance(a))