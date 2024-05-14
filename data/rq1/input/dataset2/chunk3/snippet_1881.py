#Source: https://stackoverflow.com/questions/25985508/typeerror-argument-of-type-nonetype-is-not-iterable-python
import csv
def CreateDictionary ():
    fo = open("textToEnglish2014.csv" , "r")
    dictonary = {}
    reader = csv.reader(fo)
    for row in reader:
        dictionary[row[0]] = row[1]
        return dictionary

def main():
    dictionary = CreateDictionary()
    y = "y"
    while y == "y":
        text = input("Enter text to which you would like conversion: ")
        text = text.lower()
        ntext = text.split(" ")
        new_text = ""
        x = 0
        while x < len(ntext):
            if ntext[x] in dictionary:
                new_text = new_text + dictionary[ntext[x]] + " "
            else:
                export = export + "NF "
            x += 1
        print (new_text)
        y = input("Continue conversion? y or q ")

main()