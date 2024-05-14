#Source: https://stackoverflow.com/questions/46173323/getting-error-on-frequency-distribution-typeerror-unhashable-type-list
doc_clean = []
stopwords_corpus = UrduCorpusReader('./data', ['stopwords-ur.txt'])    
stopwords = stopwords_corpus.words()
# print(stopwords)
for infile in (wordlists.fileids()):
    words = wordlists.words(infile)
    print(infile)
    #print(words)
    finalized_words = remove_urdu_stopwords(stopwords, words)
    print("\n==== WITHOUT STOPWORDS ===========\n")
    print(finalized_words)
    doc_clean.append(finalized_words)
fdist1 = FreqDist(doc_clean) 
print(fdist1) 