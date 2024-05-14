#Source: https://stackoverflow.com/questions/46591205/accessing-an-objects-array-of-objects-attribute-gives-attribute-error-in-python
class Thing:
    def __init__(self, attribute1='y', attribute2='n'):
        self.attribute1, self.attribute2 = attribute1, attribute2
    def give_a_thing(self):
        return self

class ThingOfThings:
    def __init__(self, items=[]):
        self.items = items
    def get_thing(self, thing):
        self.items += [thing]

list_of_things = ThingOfThings()

one_thing = Thing()
for i in range(2):
    list_of_things.get_thing(one_thing.give_a_thing)
print(list_of_things.items[0].attribute1)