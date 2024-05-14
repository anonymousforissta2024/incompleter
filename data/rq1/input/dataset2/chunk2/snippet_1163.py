#Source: https://stackoverflow.com/questions/51153553/not-returning-updates-to-yaml-file-and-returning-typeerror-on-string-update
f = {'A': 7, 'B':{'C':'D', 'D':False, 'E':'Julio'},\
         'The Real C': {'J?':'Yes, this is J.', 'K' : 241},'Q' : 2}

#TypeError: 'int' object is not iterable.
test.update_value(f)