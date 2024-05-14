#Source: https://stackoverflow.com/questions/60878353/reading-json-object-typeerror-io-textiowrapper-object-is-not-subscriptable
feeds = []
i = 0
for feed in output['posts']:
    feed['id'] = i
    print(feed['id'], str(feed['title']))
    i += 1
    feeds.append(feed)