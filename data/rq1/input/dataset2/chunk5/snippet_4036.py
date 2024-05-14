#Source: https://stackoverflow.com/questions/53284528/importing-file-with-constants-and-throwing-attributeerror-python-3
import settings
import dataAccquisition as da

data = []

def getData():
    global data
    print(' : [MSG] : Starting up...')
    da.getFile()
    data = da.parseData()
    print(' : [MSG] : Start up done, ready to be used.')

def getRate(currencyName):
    return data[currencyName]

def menu():
    def text():
        print('''\n----------------MENU----------------
-    0. Convert currency           -
-    1. Display all rates          -
-    2. Retry to download data     -
-    3. Quit                       -
------------------------------------''')
    run = True
    while run:
        text()
        choice = input('s: ')
        if choice == '0':
            for currency, rates in data.items():
                print("'"+str(currency)+"'",":","to"+str(currency)+",")
        elif choice == '1':
            for currency, rates in data.items():
                print(currency,':', rates)
        elif choice == '2':
            getData()
        elif choice == '3':
            run = False
            # sys.quit()
        else:
            print(' : [MSG] : No such choice!')
            choice = input('s: ')

def toUSD():
    pass

def toJPY():
    pass

def toBGN():
    pass

def toCZK():
    pass

def toDKK():
    pass

def toGBP():
    pass

def toHUF():
    pass

def toPLN():
    pass

def toRON():
    pass

def toSEK():
    pass

def toCHF():
    pass

def toISK():
    pass

def toNOK():
    pass

getData()
menu()