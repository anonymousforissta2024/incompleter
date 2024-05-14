#Source: https://stackoverflow.com/questions/69014725/why-is-self-age-showing-attribute-error-whilst-the-use-of-only-age-in-condition
class student_list:
    class_membership=True
    def __init__(self,name,age,miles):
        if self.age>=18:
            self.name=name
            self.age=age
            self.miles=miles

    def run(self):
        print(f'I ran {self.miles}')

    def name_1(self):
        print(f'Hi my name is {self.name}')

player_1=student_list('Tom Ellis',20,20)
print(player_1.name)
print(player_1.age)