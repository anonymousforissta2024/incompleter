#Source: https://stackoverflow.com/questions/61904073/nameerror-name-word-is-not-defined-python
words = [stemmer.stem(w.lower()) for w in word.split() for word in words if word not in ignore]