#Source: https://stackoverflow.com/questions/49926774/gensim-word2vec-model-wv-index2word-typeerror-slice-indices-must-be-integers-o
with open("metadata.tsv", "w+") as file_metadata:
    for i,word in enumerate(model.wv.index2word[:max]):
        w2v[i] = model.wv[word]
        file_metadata.write(word + "\n")