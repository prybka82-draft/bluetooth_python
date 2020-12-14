import pygatt
from binascii import hexlify

mac = "D0:F0:18:43:F2:B7"
uuid = "04710c43-4c62-4de8-9c1b-c439689d1886"

adapter = pygatt.GATTToolBackend() # requirez BlueZ not available on Windows!!!

try:
    pass
except expression as identifier:
    pass
finally:
    pass

try:
    adapter.start()

    device = adapter.connect(mac,timeout=10.0)
    value = device.char_write_handle(handle,value=,wait_for_response=True,timeout=30)
    chars = device.discover_characteristics()

    print(f"Data received: {hexlify(value)}")
except:
	print(f"Couldn't connect to device")	
finally:
    adapter.stop()