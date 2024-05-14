#Source: https://stackoverflow.com/questions/61275826/python-trying-to-randomly-select-the-value-from-list-within-a-list-results-in-th
import random
import string

def passwordGenerator():
    lowerchars      =   list(string.ascii_lowercase)
    upperchars      =   list(string.ascii_uppercase)
    speciachars     =   ['&','!','_','@']
    numericchars    =   list(range(0,9))
    otherrandom     =   list(string.ascii_lowercase, string.ascii_uppercase, range(0,9), ['&','!','_','@'])
    #otherrandom     =   list(list(string.ascii_lowercase), list(string.ascii_uppercase) list(range(0,9)), ['&','!','_','@'])
    print(random.choice(otherrandom))
    #print(random.choice(random.choice(otherrandom)))
    password        = random.choice(lowerchars) + random.choice(upperchars) + random.choice(speciachars) + str(random.choice(numericchars))

passwordGenerator()