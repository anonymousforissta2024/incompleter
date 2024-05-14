#Source: https://stackoverflow.com/questions/38986341/python-nameerror-name-is-not-defined-related-to-having-default-input-argument
#-------------------------------------------------------------------
#EXAMPLES:
#-------------------------------------------------------------------
#Only executute this block of code if running this module directly,
#*not* if importing it
#-see here: http://effbot.org/pyfaq/tutor-what-is-if-name-main-for.htm
if __name__ == "__main__": #if running this module as a stand-alone program
    import random
    random.seed(0)

    bytes = bytearray(100)
    for i in range(len(bytes)):
        bytes[i] = int(random.random()*256)

    print(list(bytes)); print();

    print('built-in method:')
    print(bytes.find(255))
    print(bytes.find(2,10,97))
    print(bytes.find(5,97,4))

    print('\ncircularFind:')
    print(circularFind(bytes,255))
    print(circularFind(bytes,2,10,97))
    print(circularFind(bytes,5,97,4))