#Source: https://stackoverflow.com/questions/48094827/typeerror-not-supported-between-instances-of-nonetype-and-str-using-pyn
import ner
tagger = ner.SocketNER(port=9191, output_format='slashTags')
t = "My daughter Sophia goes to the university of California. James also goes there"
print(type(t))
test = tagger.get_entities(t)
person_ents = test['PERSON']
for i in person_ents:
    print(i)