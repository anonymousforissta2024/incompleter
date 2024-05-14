#Source: https://stackoverflow.com/questions/62600155/new-to-python-typeerror-not-supported-between-instances-of-str-and-int
name = 'Bob'
age = '3000'
if name == 'Alice':
    print ('Hi Alice')
elif age < 12:
    print ('you are not Alice.')
elif age > 2000:
    print ('unlike you, ALice is no an undead, immortal vampire')
elif age > 100:
    print ('You are not Alice, Granny.')