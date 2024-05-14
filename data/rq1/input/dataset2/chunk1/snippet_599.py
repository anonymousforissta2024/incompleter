#Source: https://stackoverflow.com/questions/63479213/attributeerror-nonetype-object-has-no-attribute-lower
vectorizer = CountVectorizer(tokenizer = lambda x: x.split(" "))

tag_dtm = vectorizer.fit_transform(tag_data['Tags'])