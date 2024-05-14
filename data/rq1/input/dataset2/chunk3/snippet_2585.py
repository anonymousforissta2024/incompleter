#Source: https://stackoverflow.com/questions/57953013/typeerror-unorderable-types-int-str
json_file = open("./Labeled.json","r",encoding="utf-8")
data = json.load(json_file)

if __name__ == '__main__':
    # logger setup
    log = logging.getLogger('GiveMe5W')
    log.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    log.addHandler(sh)

    # giveme5w setup - with defaults
    extractor = MasterExtractor()
    Document() 

for i in range(0,1000):
    body = data[i]["body"]
    #print(body)
    #for line in body:
    #print(line[0:line.find('\n')])
    #head = re.sub("[^A-Z\d]", "", "")
    head = re.search("^[^\n]*", body).group(0)
    head = str(head)

    title = data[i]["title"]
    title = str(title)

    body = data[i]["body"]
    body = str(body)

    published_at = data[i]["published_at"]
    published_at = str(published_at)

    doc1 = Document(title,head,body,published_at)


    doc = extractor.parse(doc1)