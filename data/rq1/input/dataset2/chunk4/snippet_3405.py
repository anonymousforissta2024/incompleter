#Source: https://stackoverflow.com/questions/76192885/attributeerror-module-nltk-has-no-attribute-suggest
import nltk
nltk.download('udhr')
from nltk.corpus import udhr
nltk.corpus.udhr.fileids()
somali_text = nltk.corpus.udhr.raw('Somali-Latin1')
len(somali_text)
words = list(somali_text)
print(words)
#dictionary that maps each word to its frequency

frequence_dict = {}
for word in words:
  if word not in frequence_dict:
    frequence_dict[word] = 1
  else:
    frequence_dict[word] += 1

#sorting the dictionary by frequency

sorted_frequency_dict = sorted(frequence_dict.items(), key = lambda x: x[1], reverse = True)

#misspelled words
misspelled_words = []
for word, frequency in sorted_frequency_dict:
  if frequency < 3:
    misspelled_words.append(word)
  
#corrections for misspelled words

corrections = {}
for misspelled_word in misspelled_words:
  corrections[misspelled_word] = nltk.suggest(misspelled_word)