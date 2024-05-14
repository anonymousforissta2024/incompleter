#Source: https://stackoverflow.com/questions/61624362/nameerror-name-synset-is-not-defined
print("Array..............\n\n")
tagged=np.array(df['tagged_texts'])
temp = []
for x in tagged: 
    for y in x: 
        temp.append(y) 
tagged = temp
print(tagged)
pos=neg=obj=count=0
for word, tag in tagged:
    ss_set = []
    if 'NN' in tag and swn.senti_synsets(word):
        ss_set = list(swn.senti_synsets(word))
    elif 'VB' in tag and swn.senti_synsets(word):
        ss_set = list(swn.senti_synsets(word))[0]
    elif 'JJ' in tag and swn.senti_synsets(word):
         ss_set = list(swn.senti_synsets(word))[0]
    elif 'RB' in tag and swn.senti_synsets(word):
         ss_set = list(swn.senti_synsets(word))[0]
    if ss_set:
        pos=pos+synset.pos_score()
        neg=neg+synset.neg_score()
        obj=obj+synset.obj_score()
        count+=1
final_score=pos-neg
print(final_score)
df['final_score']=final_score