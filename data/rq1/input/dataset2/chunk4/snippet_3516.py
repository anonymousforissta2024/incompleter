#Source: https://stackoverflow.com/questions/72254923/python-attributeerror-object-has-no-attribute-pointing-to-constructor-error
from BaseballPlayer import BaseballPlayer
from CustomExceptions import InvalidPlayerNumException
from CustomExceptions import InvalidBattingException

# Try/except block
try:
    name = input("Enter name: ")
    number = int(input("Enter number: "))
    position = input("Enter position: ")
    batting_avg = float(input("Enter batting average: "))

    # create an instance of a baseball player
    my_player = BaseballPlayer(name, number, position, batting_avg)

    # invoke the to_string() method and display everything
    print(my_player.to_string())

# Exception handling, always go from most specific exception to most generic
except InvalidPlayerNumException as e:
    print("Invalid player number: ", e)
except InvalidBattingException as e:
    print("Invalid batting avg: ", e)

# generic exception
except Exception as ex:
    print("Generic exception: ", ex)