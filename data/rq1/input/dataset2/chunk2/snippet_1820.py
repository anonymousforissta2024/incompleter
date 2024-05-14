#Source: https://stackoverflow.com/questions/30912607/python3-csv-dictwriter-writing-through-bz2-fails-typeerror-str-buffer-inter
from csv import DictWriter
import bz2

FIELDNAMES = ('a', 'b')
OUT_BZ2 = 'out.csv.bz2'

DATA = ({'a': 1, 'b': 2}, {'a':3, 'b':4})

# this fails
with bz2.open(OUT_BZ2, mode='w', compresslevel=9) as file_pointer:
    csv_writer = DictWriter(file_pointer, fieldnames=FIELDNAMES)
    csv_writer.writeheader() # fails here; raises "TypeError: 'str' does not support the buffer interface"
    for dataset in DATA:
        csv_writer.writerow(dataset)