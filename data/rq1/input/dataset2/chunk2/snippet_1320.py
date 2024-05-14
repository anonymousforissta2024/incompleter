#Source: https://stackoverflow.com/questions/48192796/typeerror-int-object-is-not-iterable-error-in-python
counter = 0
for i in len(s):
    if i in ('a','e','i','o','u'):
        counter += 1
print("Number of vowels:" + str(counter))