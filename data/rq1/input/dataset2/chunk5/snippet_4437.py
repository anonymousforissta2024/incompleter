#Source: https://stackoverflow.com/questions/74600872/attributeerror-list-object-has-no-attribute-lower-how-to-fix-the-code-in-o
def removeDigits(str):
    return str.translate({ord(i): None for i in '0123456789'})

def fileinput():
    with open('constant.txt') as f:
        lines = f.readlines()
    
    print('Initial string: ', lines)
    res = list(map(removeDigits, lines))
    print('Final string: ', res)
    
    print('Make string upper or lower?')
    choice = input()
    if choice.upper() == 'UPPER':
        print(res.upper())
        
    elif choice.lower() == 'lower':
        print(res.lower())
    else:
        print('An error has occured')
    

fileinput()