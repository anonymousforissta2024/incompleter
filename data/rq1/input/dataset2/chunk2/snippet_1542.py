#Source: https://stackoverflow.com/questions/66814114/python-attributeerror-io-textiowrapper-object-has-no-attribute-append-er
for i in range(100):
    with open("New Text Document.txt", "a") as f:
        f.append("Q.) \n")