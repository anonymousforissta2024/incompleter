#Source: https://stackoverflow.com/questions/65199374/typeerror-a-bytes-like-object-is-required-not-str-when-trying-to-write-in-cs
with open('C:/path_to_csv_file/fold1_1.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row, timeseq in izip(fold1, fold1_t):
        spamwriter.writerow([unicode(s).encode("utf-8") +'#{}'.format(t) for s, t in izip(row, timeseq)])