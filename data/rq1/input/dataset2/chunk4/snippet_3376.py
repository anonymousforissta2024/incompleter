#Source: https://stackoverflow.com/questions/68641918/attributeerror-character-object-has-no-attribute-set-name
from Classes.character import character
from functions.yesorno import _yesorno
#character
char = character()
while True:
  print("please enter a name for your character")
  char.set_name(input())
  print("Your name is: " + char.name + ". Are you happy with your choice? Type 'y' for yes, 'n' for no.")
  if _yesorno(input()):
    break
  else:
    next