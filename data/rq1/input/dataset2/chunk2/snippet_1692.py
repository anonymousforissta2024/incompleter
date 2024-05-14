#Source: https://stackoverflow.com/questions/38986341/python-nameerror-name-is-not-defined-related-to-having-default-input-argument
def circularFind(myByteArray, searchVal, start=0, end=len(myByteArray)):
    """
    Return the first-encountered index in bytearray where searchVal 
    is found, searching to the right, in incrementing-index order, and
    wrapping over the top and back to the beginning if index end < 
    index start
    """
    if (end >= start):
        return myByteArray.find(searchVal, start, end)
    else: #end < start, so search to highest index in bytearray, and then wrap around and search to "end" if nothing was found 
        index = myByteArray.find(searchVal, start, len(myByteArray))
        if (index == -1):
            #if searchVal not found yet, wrap around and keep searching 
            index = myByteArray.find(searchVal, 0, end)
        return index 