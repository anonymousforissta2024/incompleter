#Source: https://stackoverflow.com/questions/47847807/typeerror-expected-string-or-bytes-like-object-while-filtering-the-nested-list
pattern = re.compile(r'\W+')
newlist = list(filter(pattern.search, list))
print(newlist)