#Source: https://stackoverflow.com/questions/43657351/typeerror-a-bytes-like-object-is-required-not-str-error-getting
import csv

fin = open('another_summary_table.csv')
words = ["PCB","Switch","Socket","Red-Green LED","Solar Panel","Battery", "Load wire"]
found = {}

wr = csv.writer(open("boop-1.csv", "wb"))
fieldnames = ['PartsReplaced']
writer = csv.DictWriter(fin, fieldnames=fieldnames)
for line in fin:
    split_line=line.split(',')
    str1=split_line[2] # Whatever columns
    PartsReplaced=split_line[2] # Whatever columns

    for w in words:
        if w in str1:
            found[w]=found.get(w,0)+1

            break
wr.writerows(found)