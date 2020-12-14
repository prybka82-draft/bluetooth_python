
from __future__ import print_function
import pygatt
from binascii import hexlify
import logging
import uuid
import time

logging.basicConfig()
logging.root.setLevel(logging.INFO)

addr_type = pygatt.BLEAddressType.random
mac = "D0:F0:18:43:F2:B7"
uuid_no = "04710c43-4c62-4de8-9c1b-c439689d1886"
uuid_ha = "02290000-0000-0000-0000-000000000000"
uuid_ha = "00000000-0000-0000-0000-000000002902"
handle = bytearray([0x01, 0x00])


def data_handler(handle,value):
   print(value)
   #print("Data received: {hexlify(value)}")

def foo(par: str) -> str:
    pass

def discover_characteristics(device, logging):
   logging.info("Discovering characteristics")
   chars = device.discover_characteristics().keys()

   logging.info("Discovered {} characteristics".format(len(chars)))
   chars = device.discover_characteristics().keys()

   pygatt.device.BLEDevice.get_rssi()

   for u in chars:
      #print("\tUUID: {}: {}".format(u, binascii.hexlify(device.char_read(u))))
      print(u)


logging.info("Creating adapter")
adapter = pygatt.GATTToolBackend()

try:
   logging.info("Starting adapter")
   adapter.start()

   logging.info("Connecting to device")
   device = adapter.connect(mac)
   logging.info("Connected!")

   #discover_characteristics(device, logging)

   logging.info("Writing values to characteristic")
   #device.subscribe(uuid=uuid_no,callback=data_handler,wait_for_response=True)
   #device.char_write_handle(uuid_no, bytearray([0x01, 0x00]), wait_for_response=True)
   #device.char_write_handle(handle=data_handler, value=bytearray([0x01, 0x00]), wait_for_response=True)
   #device.char_write("0x2902", bytearray([0x01, 0x00]))
   #device.char_write(bytearray([0x29, 0x02]), bytearray([0x01, 0x00]))
   #device.char_write(bytearray(b'\x29\x02'), bytearray(b'\x01\x00'))
   #device.char_write(bytearray(b'\x29\x02'), bytearray([0x01, 0x00]))
   #device.char_write(uuid_ha, bytearray([0x01, 0x00]))
   #device.char_write(uuid_no, bytearray([0x01,0x00]))
   logging.info("Values written")


   #logging.info("Bonding")
   #device.bond() #gryzie się z device.char_read
   #logging.info("Bonded")

   logging.info("Reading characteristic")
   #device.char_read_handle(handle=data_handler, timeout=5)
   #device.char_read(uuid_no, timeout=5)
   #value = device.char_read(uuid_no)
   #print(value)
   logging.info("Characteristic read")

   time.sleep(5)
   device.subscribe(uuid_no, callback=data_handler,indication=True)
   time.sleep(5)

   logging.info("Subscribed")

   while 1:
      pass

   #value = device.char_read(uuid_no)
   #print(value)


   #device.char_write_handle(handle,wait_for_response=true)
   #device.subscribe(uuid_no, callback=data_handler)

   #logging.info("Data received: {}".format(hexlify(value)))

   #res = device.char_write('0x2901',handle,true)
   #print(res)

   #device.subscribe(uuid_no, callback=data_handler,indication=true)

except Exception as e:
   print("Couldn't connect to device")
finally:
   logging.info("Stopping adapter")
   adapter.stop()





