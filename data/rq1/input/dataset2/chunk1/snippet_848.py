#Source: https://stackoverflow.com/questions/65592003/how-to-fix-typeerror-cant-pickle-module-objects-during-multiprocessing
for sc in scans:
    my_file = scans[sc].resources['DICOM'].files[0]