#Source: https://stackoverflow.com/questions/65592003/how-to-fix-typeerror-cant-pickle-module-objects-during-multiprocessing
def process(x):
    my_file = x.resources['DICOM'].files[0] 

def another_method():
    ...                
    pool = Pool(os.cpu_count())
    pool.map(process, [scans[sc] for sc in scans])

another_method()  