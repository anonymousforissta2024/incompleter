#Source: https://stackoverflow.com/questions/57756344/attributeerror-modbusioexception-object-has-no-attribute-registers
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

# mbClient = ModbusClient(method = "rtu", port="COM4", stopbits = 1, bytesize = 8, parity = 'N', baudrate = 9600)
mbClient = ModbusClient(method = "rtu", port="COM4")
mbClient.connect()

totalEnergy = mbClient.read_holding_registers(0x0000, 2, unit=1)
print(totalEnergy.registers)
mbClient.close()