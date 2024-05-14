#Source: https://stackoverflow.com/questions/73418212/attributeerror-module-networkx-has-no-attribute-nx-pydot
serial_no = str(i)
document = open('DataSet/Source/'+serial_no+'.txt').read()
doc = sentTokenizer.sentTokenizing().sentTokenize(document)
print('doc',doc)

filenamee, n = clustering.startF(doc)
print("\n\nSource:",document)

summary = getSummary(filenamee)
print('\n\nSummary:',summary)

# save the summary
createFolder('DataSet/')
fi = open('DataSet/'+serial_no+'.txt','+w')
fi.write(summary)