#Source: https://stackoverflow.com/questions/65543733/python-typeerrorstring-argument-without-an-encoding
sent_message = network_connect_join.send(bytes(sending_message)).encode('utf-8')