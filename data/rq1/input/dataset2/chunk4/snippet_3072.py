#Source: https://stackoverflow.com/questions/68638629/json-dump-typeerror-object-of-type-int64-is-not-json-serializable
ldamodel = LDA_Model(data_words)
coherence = ldamodel.build_models(start = 5, limit= 71, step= 5, runs=10)