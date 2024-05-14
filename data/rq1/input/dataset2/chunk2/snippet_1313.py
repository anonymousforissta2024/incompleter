#Source: https://stackoverflow.com/questions/72952618/error-message-through-data-readout-of-an-opc-ua-node-attributeerror-str-obj
client.connect()

forceAS = client.get_node("ns=3;g=V:0.3.0.0.1")
meaForceAS = forceAS.get_data_value() # here I get the error