#Source: https://stackoverflow.com/questions/65839209/typeerror-can-only-concatenate-list-not-str-to-list-create-a-script-that-co
import re
inputList = []
for file in ['text1.txt','text2.txt']:
    with open(file,'r') as infile:
        k = 0
        for line in infile:
            i = 0
            if i < len(inputList) and k:
                inputList[i].extend(re.sub('[^A-Za-z0-9,]+', '', line).split(","))
            else :
                inputList.append(re.sub('[^A-Za-z0-9,]+', '', line).split(","))
            i += 1
        k = 1
print(inputList)
with open('text3','w') as outfile:
    for line in inputList:
        outfile.write(line + '\n')