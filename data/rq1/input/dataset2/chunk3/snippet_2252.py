#Source: https://stackoverflow.com/questions/58681634/python3-error-typeerror-str-object-is-not-callable
url = "https://www.reddit.com/r/" + subreddit + "/" + feed + ".json?sort=" + feed + "&limit=6"

resp = requests.get(url, verify=False)
json = json.loads(resp.text())

print(json["data"]["children"][0]["data"]["id"])