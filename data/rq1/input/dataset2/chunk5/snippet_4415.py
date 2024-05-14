#Source: https://stackoverflow.com/questions/59314321/interactive-dictionary-typeerror-dict-not-callable
import json

data = json.load(open("files1\data.json"))

def definitioner(w):
    return data(w)

word = input("Enter the word you are looking for: ")
print(definitioner(word))