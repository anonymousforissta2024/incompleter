#Source: https://stackoverflow.com/questions/74460778/how-do-i-fix-typeerror-must-be-a-real-number-not-a-tuple-error
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car1.name = "Fer"
car1.color = "Red"
car1.kind = "Convertible"
car1.value = 60,000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "Blue"
car2.kind = "Van"
car2.value = 10,000.00

print(car1.description())
print(car2.description())