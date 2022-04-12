from pyModbusTCP.client import ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
import time

modbus_address = 30001

try:
  global client
  client = ModbusClient("192.168.100.137", 502, 3)
  client.close()

  client.open()
except:
  print("SMA Inverter connection problem")
loop=0

while modbus_address < 50000:
  try:
    valueread = client.read_holding_registers(modbus_address, 2)
    value = BinaryPayloadDecoder.fromRegisters(valueread, Endian.Big, Endian.Big).decode_32bit_uint()
    print(modbus_address,"=",value)
    modbus_address += 2
    time.sleep(0.1)
  except:
    modbus_address += 2

client.close()
