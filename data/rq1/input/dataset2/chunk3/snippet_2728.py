#Source: https://stackoverflow.com/questions/68092717/i-am-trying-to-append-a-dictionary-to-a-list-but-it-showing-me-name-error-and-t
class Category:
    ledger =[]
    
    def __init__(self,category):
        print(category)
       

    def deposit(self,amount,description):
        
        self.amount=amount
        self.description=description
        if not description:
            return ""
        else:
        
            dect={"amount":self.amount,"description":self.description}
            print(dect)
            ledger.append(dect)
            self.ledger=ledger
            print(self.ledger)
food=Category("food")
food.deposit(1000,"initial deposit")