#Source: https://stackoverflow.com/questions/51153553/not-returning-updates-to-yaml-file-and-returning-typeerror-on-string-update
b = {'A': '', 'B':{'C':'D', 'D':False, 'E':'Julio'},\
         'The Real C': {'J?':'Yes, this is J.', 'K' : 241},'Q' : 'PQ'}

#TypeError: string indices must be integers.
test.update_value(b)