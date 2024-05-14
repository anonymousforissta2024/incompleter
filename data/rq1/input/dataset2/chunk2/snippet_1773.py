#Source: https://stackoverflow.com/questions/49814731/typeerror-write-argument-must-be-str-not-bytes-python
with open('vocabulary-embedding.pickle', 'wb') as f:
    pickle.dump((embedding, idx2word, word2idx),f,-1)