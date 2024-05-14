#Source: https://stackoverflow.com/questions/53755893/facing-attributeerror-for-tag-using-spacy-in-python
import pandas as pd
read_data = pd.read_csv('C:\\Users\\abc\\def\\pqr\\Data\\training_data.csv', encoding="utf-8")
entity = []
for parsed_doc in read_data['Description']:
    doc = nlp(parsed_doc)
    a = [(X.text, X.tag_) for X in doc.ents]
    entity.append(a)