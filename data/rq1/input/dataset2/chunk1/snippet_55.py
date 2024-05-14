#Source: https://stackoverflow.com/questions/22121108/encoding-type-error-python-3-x
inputfilename = "a.txt"
outputfilename = inputfilename[0:-4]+"_fixed"+".txt"

inputfile = open(inputfilename, 'r')

str = inputfile.read() #name for the file

newstring = str.replace("œ", "s").replace("ê","e").replace("³","l").replace("¹","a").replace("¿","z").replace("ñ","n").replace("Ÿ","z").replace("æ","c")

outputfile = open(outputfilename, "w")
outputfile.write(newstring)
outputfile.close()