#Source: https://stackoverflow.com/questions/74713051/attributeerror-modbusioexception-object-has-no-attribute-bits
from pymodbus.client import ModbusTcpClient

PLC_IP = '192.168.0.200'
PLC_PORT = 502
client = ModbusTcpClient(PLC_IP, PLC_PORT)
status = client.connect()
print(status)
result = client.read_coils(1,5)
if result.bits[0] == True:
    print("Hello world")
client.close()