#Source: https://stackoverflow.com/questions/59111440/python3-cannot-import-local-module-due-to-filenotfounderror
import urllib.request, re, os

def getKey(url, path):
    urllib.request.urlretrieve(url, 'C:\\code\\'+path)

def readFiles(keyFile, targetFile, outfile):
    infile = keyFile                                            # read in the input file name
    infd = open('C:\\code\\'+infile,"r")                     # open the file and create the file descriptor infd

    key = infd.read( )
    key = key.strip('\n')
    #print('key= '+key)

    infile = targetFile
    infd = open('C:\\code\\'+infile, "r")
    ptext = infd.read( ).strip('\n')

    infd.close

    xor(outfile, ptext, key)

def xor(outfile, ptext, key):
    outfd = open('C:\\code\\'+outfile, "w")

    pLength = len(ptext)

    #get the length of the plaintext and cut the key into the same size
    keyChunks = [key[i:i+pLength] for i in range(0, len(key), pLength)]

    i = 0

    while i < len(keyChunks):
        a = int(ptext)
        b = int(keyChunks[i])

        out = a ^ b

        i=i+1

    outfd = open('C:\\code\\'+outfile, "w")
    outfd.write(str(out))
    outfd.close

def cleanup(targetFile):
    os.remove(targetFile)


def enc():
    outfile = 'affk.xor'
    getKey('http://192.168.56.10/sym.key', 'sym.key')
    readFiles('sym.key', 'affk.txt', outfile)
    cleanup('C:/code/affk.txt')

def dec():
    outfile = 'affk.txt'
    getKey('http://192.168.56.10/sym.key', 'sym.key')
    readFiles('sym.key', 'affk.xor', outfile)
    cleanup('C:/code/affk.xor')
    cleanup('C:/code/sym.key')

enc()
#dec()