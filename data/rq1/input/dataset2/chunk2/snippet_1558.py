#Source: https://stackoverflow.com/questions/47824780/saving-data-into-solr-with-pysolr-get-rejected-attributeerror-str-object-has
from solrq import Q
import pysolr
import jsonpickle
from datetime import datetime, timedelta
from Model import Twitter



#conexion a solr
solr = pysolr.Solr('http://localhost:8983/solr/twitter')

#query
query = Q(label="none")
results = solr.search(query)


print("Saw {0} result(s).".format(len(results)))

#testing the query
for result in results:
    print("-->".format(result['content']))

#creating a new class with data    
twit = Twitter("000002","content text","some label")  
#list of twitter classes
coreData=[]

coreData.append(twit)
#encoding to json
json=str(jsonpickle.encode(coreData, unpicklable=False))

print(json)
#saving to solr
solr.add(json)