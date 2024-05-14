#Source: https://stackoverflow.com/questions/58254427/typeerror-decoding-str-is-not-supported-typeerror-decoding-str-is-not-supporte
ww2 = u'''
World War II (often abbreviated to WWII or WW2), also known as the Second World War, was a global war that lasted from 1939 to 1945, although related 
'''
ww2 = unicode(ww2, 'utf-8')

ww2b = TextBlob(ww2)