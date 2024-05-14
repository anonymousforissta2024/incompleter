#Source: https://stackoverflow.com/questions/54620191/list-comprehension-returntypeerror-string-indices-must-be-integers
with open ('/Users/Weindependent/Desktop/dataset/albumlist.csv', encoding='cp1252') as case0:
    reader = csv.DictReader(case0) #the file is coded with single-byte coding
    album = []
    for row in reader:
        album.append(row)
print (len(album))