#Source: https://stackoverflow.com/questions/38994825/typeerror-unsupported-operand-types-for-or-pow-int-and-str
play = True

while play:

    x = input("Enter a number: ")
    y = input("Enter a number: ")

    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x % y)

    if input("Play again? ") == "no":
        play = False