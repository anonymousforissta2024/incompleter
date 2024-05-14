#Source: https://stackoverflow.com/questions/64922421/attributeerror-tuple-object-has-no-attribute-get-in-python-3
for i in range(len(uniquecandidate)):
    result = zip(uniquecandidate, votes) # zips two lists together  

result_list = list(result)
print(type(result_list))   # returns <class 'list'>

result_list.sort(key=lambda x: x.get('votes'), reverse=True) #sort by vote number

print(result_list, end='\n\n')
                                                   