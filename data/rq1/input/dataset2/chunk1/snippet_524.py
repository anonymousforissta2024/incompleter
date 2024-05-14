#Source: https://stackoverflow.com/questions/70646480/iterating-through-directory-error-filenotfounderror-errno-2-no-such-file-or
import os
import sys
import nltk
nltk.download()
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import io

files_path = sys.argv[1]
textfile_dictionary = sys.argv[2]

for filename in os.listdir(files_path):
    if filename.endswith(".txt"):

        #accessing file for processing
        file = open(filename, "rt")
        text = file.read()

        #tokenize text file
        tokens = word_tokenize(text)

        #remove non-alphabetical characters
        words = []

        for word in tokens:
            if word.isalpha():
                words.append(word)

        #remove stopwords
        stop_words = stopwords.words("english")
        words_without_stops = []

        for w in words:
            if not w in stop_words:
                words_without_stops.append(w)
                

        #lemmatize remaining tokens and print
        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for x in words_without_stops:
            lemmatizer.lemmatize(x)
            lemmas.append(x)

        #turn dictionary held in text file into a list of tokens
        file = io.open(textfile_dictionary, mode="r", encoding="utf8")
        dictionaryread = file.read()
        dictionary = dictionaryread.split()

        #count instances of each word in dictionary in the novel and add them up
        word_count = 0

        for element in dictionary:
            for lemma in lemmas:
                if lemma == element:
                    word_count = word_count + 1

        print(word_count)