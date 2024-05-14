#Source: https://stackoverflow.com/questions/48917449/typeerror-a-bytes-like-object-is-required-not-str-when-converting-gensim-to
with open(outfiletsv, 'w+b') as file_vector:
    with open(outfiletsvmeta, 'w+b') as file_metadata:
        for word in model.index2word:
            file_metadata.write(gensim.utils.to_utf8(word) + gensim.utils.to_utf8('\n'))
            vector_row = '\t'.join(str(x) for x in model[word])
            file_vector.write(vector_row + '\n')