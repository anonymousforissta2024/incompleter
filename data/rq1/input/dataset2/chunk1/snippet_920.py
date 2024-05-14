#Source: https://stackoverflow.com/questions/67300476/attribute-error-in-python-object-has-no-attribute
class Person:
    def __init__(self, name, age, occupation):
      self.name = name
      self.age = age
      self.occupation = occupation
  
    def say_hello(self):
      print(f"Hello, my name is {self.name}.")
  
    def say_age(self):
      print(f"I am {self.age} years old.")
    
class Superhero(Person):
    def __init__(self, name, age, occupation, secret_identity, nemesis):
      self.secret_identity = secret_identity
      self.nemesis = nemesis

hero = Superhero("Spider-Man", 17, "student", "Peter Parker", "Green Goblin")
print(hero.name())