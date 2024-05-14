#Source: https://stackoverflow.com/questions/50166133/typeerror-classification-missing-1-required-positional-argument-gender
class HumanClassification:
    def __init__(self):
        self.age = 0
        self.height = 0
        self.gender = []
    def classification(self, age, height, gender):
        self.age = age
        self.height = height
        self.gender = gender

bob = HumanClassification.classification(32, 6, 'male')
print (bob.age)