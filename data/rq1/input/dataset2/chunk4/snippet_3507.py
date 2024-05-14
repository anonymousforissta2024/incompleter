#Source: https://stackoverflow.com/questions/71395086/typeerror-expected-string-or-bytes-like-object-when-setting-cookies-gotten-fr
cookies = pickle.load(open("cookies.pkl", "rb"))

r = requests.Session()
for cookie in cookies:
    r.cookies.set(cookie['name'], cookie['value'])