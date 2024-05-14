#Source: https://stackoverflow.com/questions/32880712/grouping-anagrams-using-ordereddictionary-typeerror-issue
import sys
from collections import *
def findAnagrams(string):
    anagramDict = OrderedDict(list)
    for word in string:
        key = ''.join(sorted(word))
        anagramDict[key].append(word)
    return anagramDict

def main():
    for string in sys.stdin:
        stringList = string.split()
        if len(stringList) == 0:
           break
        anagramDict = findAnagrams(stringList)
        for key,anagrams in anagramDict.items():
            if len(anagrams) >=1:
                print(' '.join(sorted(anagrams)))
        print ()
main()