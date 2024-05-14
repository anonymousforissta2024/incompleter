#Source: https://stackoverflow.com/questions/67135036/python-json-format-error-typeerror-string-indices-must-be-integers
message = socket.recv()
 
print("DBG#80:orginal message:", message)
message_string = message.decode("utf-8")  # VVI important (it removes b" \" etc ")
print("DBG#81:message.decode('utf-8'):", message_string)
  
correlation_id_rcvd = json.dumps(message_string,separators=(',', ':'))
print("DBG#82:parsed json full=", correlation_id_rcvd)
print("DBG#83:message_correlation_id=" ,correlation_id_rcvd["message_correlation_id"])