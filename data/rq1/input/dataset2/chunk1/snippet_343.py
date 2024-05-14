#Source: https://stackoverflow.com/questions/19877306/nameerror-global-name-unicode-is-not-defined-in-python-3
# utf-8 ? we need unicode
if isinstance(unicode_or_str, unicode):
    text = unicode_or_str
    decoded = False
else:
    text = unicode_or_str.decode(encoding)
    decoded = True