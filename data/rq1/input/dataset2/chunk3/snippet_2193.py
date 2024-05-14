#Source: https://stackoverflow.com/questions/68169670/batching-python-gmail-api-attributeerror-dict-object-has-no-attribute-resu
for searchResultPart in searchResultParts: 
    batch = BatchHttpRequest() 
    batch2 = BatchHttpRequest()
    for msgID in searchResultPart: #Loop through each messageID
        request1 = service.users().messages().get(userId=userID, id=msgID).execute()
        request1.update({"resumable" : None}) #TRIED THIS DOES NOT WORK
        request2 = service.users().messages().modify(userId=userID, id=msgID, body={'removeLabelIds': ['UNREAD']}).execute()
        batch.add(request=request1,request_id=msgID) #Fetch the message
        batch2.add(request=request2,request_id=msgID) #Mark the fetched messages as read
    batch.execute() 
    batch2.execute()