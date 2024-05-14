#Source: https://stackoverflow.com/questions/56519945/i-want-to-write-json-files-with-data-that-i-scraped-with-a-webscraper-and-an-api
with open('C:/Users/Maximvs/PycharmProjects/Scrapy/planInfo/planInfo/spiders/Freedom_api.json') as json_file:
    dataRaw = json.load(json_file)
    dataText = dataRaw
    # data = json.loads(dataText)
    # print(type(dataRaw))


def writeToJSONFile(path, fileName, data):
    filePathNameWExt = '' + path + '/' + fileName + '.json'

    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


path = 'C:/Users/Maximvs/Documents/Scraper_Plans'


for Linkindex,link in enumerate(PhonePermutationLinks): #goes through all phone models and plans permutations
    fileName = str(phonesListExtended[Linkindex]) + " " + str(phonePlansListExtended[Linkindex])