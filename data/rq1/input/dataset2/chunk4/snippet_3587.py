#Source: https://stackoverflow.com/questions/64912514/filenotfounderror-even-though-the-file-exists
with open('../assets/database/database.json','r') as E:
    stuffs = json.load(E)