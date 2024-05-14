#Source: https://stackoverflow.com/questions/53426857/typeerror-typedict-object-is-not-callable
aFile  = open("A_FILE.bin", "rb")
aBytes = aFile.read()
cData  = cast(aBytes, POINTER(CData)).contents
aFile.close()