#Source: https://stackoverflow.com/questions/65199374/typeerror-a-bytes-like-object-is-required-not-str-when-trying-to-write-in-cs
with open('C:/Users/path_to_csv_file/fold1_1.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row, timeseq in zip(fold1, fold1_t): 
        for s, t in zip(row, timeseq):
            bytes_var = s.encode('utf-8') +'#{}'.format(t).encode('utf-8') 
            spamwriter.writerow(bytes_var)