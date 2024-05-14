#Source: https://stackoverflow.com/questions/71272910/attributeerror-spacy-tokenizer-tokenizer-object-has-no-attribute-tokens-from
X_train_lemma = lemma_vect.fit_transform(text_train)
print("X_train_lemma.shape: {}".format(X_train_lemma.shape))

vect = CountVectorizer(min_df=5).fit(text_train)
X_train = vect.transform(text_train)
print("X_train.shape: {}".format(X_train.shape))