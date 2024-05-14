#Source: https://stackoverflow.com/questions/61871631/typeerror-list-indices-must-be-integers-or-slices-not-re-pattern
import re

regexcode0 = re.compile(r'Test 0')
regexcode1 = re.compile(r'Test 1')
regexcode2 = re.compile(r'Test 2')

results_Test0 = []
results_Test1 = []
results_Test2 = []

allResults = [results_Test0, results_Test1, results_Test2]
regexlist = [regexcode0, regexcode1, regexcode2]

textBody = 'Hi there, Test 2 was a failure'

def text_extract(text):
    for i in regexlist:
        match = re.search(i, text)
        if match:
            matchObj = match.group()
            allResults[i].append(matchObj)

        if not match:
            allResults[i].append('No Solution')

    return allResults

print(text_extract(textBody))