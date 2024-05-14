#Source: https://stackoverflow.com/questions/44901361/python-for-starters-typeerror-not-supported-between-instances-of-str-an
print('Hi there! What is your name?')
myName = input()
print("Hello "   +  myName +  ' its good to met you. My name is Kendo.')

print('how old are you?')
myAge = input()
if myAge < 15:
    print('go to bed, kiddo')
elif myAge > 95:
    print('Sup, grandma')
elif myAge > 1000:
    print('Lol, stop kidding me')