#Source: https://stackoverflow.com/questions/30021368/python-typeerror-not-all-arguments-converted-during-string-formatting-while-rea
import rnumb
import file

def create():
    name    = input("What is your name? ")
    attack  = rnumb.randn(1,3)
    defense = rnumb.randn(1,3)
    agility = rnumb.randn(1,3)

    file.write("name",name)
    file.write("attack",attack)
    file.write("defense",defense)
    file.write("agility",agility)