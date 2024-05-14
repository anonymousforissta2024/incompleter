#Source: https://stackoverflow.com/questions/49415195/typeerror-from-multinomialnb-float-argument-must-be-a-string-or-a-number
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

#print(documents[1])

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]

def look_for_features(document):
    words = set(document)
    features = {}
    for x in word_features:
        features[x] = {x in words}
    return features

#feature set will be finding features and category
featuresets = [(look_for_features(rev), category) for (rev, category) in documents]

training_set = featuresets[:1400]
testing_set = featuresets[1400:]

#Multinomial
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print ("Accuracy: ", (nltk.classify.accuracy(MNB_classifier,testing_set))*100)