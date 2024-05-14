#Source: https://stackoverflow.com/questions/26394748/nltk-python-error-typeerror-dict-keys-object-is-not-subscriptable
fdist1 = FreqDist(NSmyText)
vocab=fdist1.keys()
vocab[:200]