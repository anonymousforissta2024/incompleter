#Source: https://stackoverflow.com/questions/59160978/unicodedata-normalize-typeerror-normalize-argument-2-must-be-str-not-list
unicodedata.normalize('NFD', line).encode('ascii', 'ignore')