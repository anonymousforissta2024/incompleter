#Source: https://stackoverflow.com/questions/59691667/why-is-it-showing-typeerror-int-object-is-not-subscriptable-in-code-snippet
ns = [21,21,13,24,45,6]
sc = sorted(set([x[1] for x in ns]))
print(sc)