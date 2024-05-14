#Source: https://stackoverflow.com/questions/62567175/python-code-for-prime-factoring-creates-a-strange-typeerror
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