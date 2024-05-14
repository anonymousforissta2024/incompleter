#Source: https://stackoverflow.com/questions/27559733/python-3-2-typeerror-argument-must-be-an-int-or-have-a-fileno-method
with open('addons.txt', 'r') as addonsFile:
    for line in addonsFile:
        addon = line.rstrip()
        fileUrl = 'http://www.google.com/%s/ncr' % addon
        response = urlopen(fileUrl)