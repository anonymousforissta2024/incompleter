#Source: https://stackoverflow.com/questions/75982209/typeerror-tradingapp-error-missing-1-required-positional-argument-advancedo
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time


class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson):
        print("Error {} {} {} {}".format(reqId,errorCode,errorString,advancedOrderRejectJson))
        
    def contractDetails(self, reqId, contractDetails):
        print("redID: {}, contract:{}".format(reqId,contractDetails))

def websocket_con():
    app.run()
    event.wait()
    #if event.is_set():
        #app.close()

event = threading.Event()   
app = TradingApp()      
app.connect("127.0.0.1", 4001, clientId=1)

# starting a separate daemon thread to execute the websocket connection
con_thread = threading.Thread(target=websocket_con)
con_thread.start()
time.sleep(1) # some latency added to ensure that the connection is established

#creating object of the Contract class - will be used as a parameter for other function calls
contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "SMART"

app.reqContractDetails(100, contract) # EClient function to request contract details
time.sleep(5) # some latency added to ensure that the contract details request has been processed
event.set()