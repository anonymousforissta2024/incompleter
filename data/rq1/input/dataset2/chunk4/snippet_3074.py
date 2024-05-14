#Source: https://stackoverflow.com/questions/76171687/save-dictionary-with-value-of-type-nltk-corpus-reader-wordnet-synset-encount
with open('dict1.pickle', 'wb') as handle:
    pickle.dump(hypernyms, handle, protocol=pickle.HIGHEST_PROTOCOL)