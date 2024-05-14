#Source: https://stackoverflow.com/questions/39146039/pickle-typeerror-a-bytes-like-object-is-required-not-str
fname1 = "auth_cache_%s" % username
fname=fname1.encode(encoding='utf_8')
#fname=fname1.encode()
if os.path.isfile(fname,) and cached:
    response = pickle.load(open(fname))
else:
    response = self.heartbeat()
    f = open(fname,"w")
    pickle.dump(response, f)