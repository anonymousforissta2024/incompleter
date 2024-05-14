#Source: https://stackoverflow.com/questions/48109184/typeerror-the-json-object-must-be-str-not-list
parsedCoin = json.loads(coin)
print(json.dumps(parsedCoin, indent=4, sort_keys=True))