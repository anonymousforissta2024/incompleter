#Source: https://stackoverflow.com/questions/53465931/string-concatenate-typeerror-can-only-concatenate-str-not-int-to-str
salaries = {'John':'20','Sally':'30','Sammy':'15'}
print(salaries['John'])

salaries['John'] = salaries['John'] + 30
print(salaries['John'])