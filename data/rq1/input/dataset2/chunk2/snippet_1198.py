#Source: https://stackoverflow.com/questions/66131209/why-is-this-valueerror-exception-used-here-and-not-typeerror-exception
try:
    val = int(userInput)
except ValueError:
    print("That's not an int!")