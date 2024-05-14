#Source: https://stackoverflow.com/questions/47249491/how-to-fix-attributeerror-module-testing2-has-no-attribute-printpackage
#testing2
import testing1
menuList = testing1.calculateMenuPrice(choice)
def printPackage(menuList):
    for x in menuList:
        if menuList == '1':
            return('''
----------
Menu List
----------
1. Jelly Fish Yee Sang with Pear
2. Dried Seafood with Fish Soup 
3. Steamed Sea Water Grouper

''')        
        elif menuList == '2':
             return('''
----------
Menu List
----------
1. Jelly Fish Yee Sang with Pear
2. Shark Fin Soup with Crab Meat
3. Steamed River Patin Fish
''')
        elif menuList == '3':
            return('''
----------
Menu List
----------
1. Salmon Fish Yee Sang with Pear
2. Steamed Classic Abalone Soup
3. Steamed Bamboo Fish

''')

        elif menuList == '4':
            return('''
----------
Menu List
----------
1. Abalone Yee Sang with Pear
2. Mini Classic Steam Soup
3. Steamed Local Pomfret Fish

''')