#Source: https://stackoverflow.com/questions/55975955/attributeerror-tuple-object-has-no-attribute-translate
mycursor = mydb.cursor()
mycursor.execute("SELECT content FROM news_tb")
myresult = mycursor.fetchall()
for row in myresult:
    row = row.translate(str.maketrans('', '', string.punctuation)).lower()


    tokens = word_tokenize(row)
    listStopword = set(stopwords.words('indonesian'))
    wordsFiltered = []

    for t in tokens:
        if t not in listStopword:
            wordsFiltered.append(t)
    print(wordsFiltered)