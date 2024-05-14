#Source: https://stackoverflow.com/questions/34905187/compression-strings-list-type-error
import zlib
sentence = input("Enter the text you want to compress: ")
listSentence = sentence.split(" ")
d = {}
i = 0
values = []
for i, word in enumerate(sentence.split(" ")):
    if not word in d:
        d[word] = (i+1)
    values += [d[word]]
coms = zlib.compress(sentence.encode('utf-8'))
comv = zlib.compress(values.encode('utf-8'))
with open("listofwords.txt", "wb") as myfile:
    myfile.write(coms)
    myfile.write(comv)