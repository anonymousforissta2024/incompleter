#Source: https://stackoverflow.com/questions/16712612/use-codecs-to-read-file-with-correct-encoding-typeerror
#!/bin/bash

import codecs

filename = "something.x10"

f = open(filename, 'r')
fEncoded = codecs.getreader("ISO-8859-15")(f)

totalLength = 0
for line in fEncoded:
  totalLength+=len(line)

print("Total Length is "+totalLength)