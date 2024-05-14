#Source: https://stackoverflow.com/questions/74278955/python-typeerror-string-indices-must-be-integers-error
articles_list = []
y= requests.get("https://hacker-news.firebaseio.com/v0/newstories.json")
y = y.json()
print(y)
print("https://hacker-news.firebaseio.com/v0/item/" + number +".json" +"?print=pretty")
for number in y:
    req = requests.get("https://hacker-news.firebaseio.com/v0/item/" + str(number) +".json" +"?print=pretty")
    req = req.json()
    print(req)
    break
for thing in req["url"]:
    articles_list.append(thing["url"])