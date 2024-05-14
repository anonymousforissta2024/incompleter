#Source: https://stackoverflow.com/questions/57448210/typeerror-update-missing-1-required-positional-argument-document
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client.Mydb
collection = db.sampledb
new_contact = "6369723748"
updatestmt = "{\"ID\" : \"12345\"},{\"$set\" :{\"ID\" : \"67891\",\"Account_Number\" : \"1234 5678 9101\"}}"
print(updatestmt)

cursor = collection.update(updatestmt)
cursor1 = collection.find()

for i in cursor1:
    print(i)