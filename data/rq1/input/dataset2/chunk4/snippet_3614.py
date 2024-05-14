#Source: https://stackoverflow.com/questions/75572426/python-oop-typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a
import csv
class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: int , quantity: int):
        #run validation to the received arguments
        assert quantity >= 0, "The {quantity} quantity should be greater or equal to zero"
        assert price >= 0, "The price should be greater or equal to zero"

        #assigned to the self object      
        self.name = name
        self.price = price
        self.quantity = quantity

        #Action to execute
        Item.all.append(self)

    def calculate_total_price(self):
       return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def intantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            # print(items)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# items


Item.intantiate_from_csv()
print(Item.all)