#Source: https://stackoverflow.com/questions/62106106/typeerror-expected-string-or-bytes-like-object-tqdm
# Combining all the above statemennts 
from tqdm import tqdm
Other_skill = []
# tqdm is for printing the status bar
for sentance in tqdm(project_data['Other skills'].values):
    sent = decontracted(sentance)
    sent = sent.replace('\\r', ' ')
    sent = sent.replace('\\"', ' ')
    sent = sent.replace('\\n', ' ')
    sent = re.sub('[^A-Za-z0-9]+', ' ', sent)
    sent = ' '.join(e for e in sent.split() if e not in stopwords)
    Other_skill.append(sent.lower().strip())