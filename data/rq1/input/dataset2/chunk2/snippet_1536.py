#Source: https://stackoverflow.com/questions/64110840/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
seqnum = None
lstFile = open(inListFileName)

for lstLn in lstFile.readlines():
    lstVals = lstLn.strip().split()

    basePath=os.getcwd()
    file=os.path.join(basePath, 'OUT_ST',lstVals[1])

    if len(lstVals) > 1:
        loadArray = np.loadtxt(file).flatten()

        if seqnum is None:
            seqnum = np.arange(1, len(loadArray) + 1)
    
        arrayTuple = map(tuple, np.column_stack((seqnum, loadArray)))
        
        strucArray = np.array(arrayTuple, np.dtype([('inSeqNum', np.int), (lstVals[0], np.float)]))
    
        arcpy.da.ExtendTable(target, seqFieldName, strucArray, 'inSeqNum', False)

lstFile.close()