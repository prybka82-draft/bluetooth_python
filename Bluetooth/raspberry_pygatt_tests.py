import pygatt.backends
from binascii import hexlify

#pygatt.exceptions.BLEError: The GATTToolBackend requires BlueZ, which is not available in Windows

def printIndication(handle, value):
    print('Indication received {} : {}'.format(hex(handle), hexlify(str(value))))

adapter = pygatt.backends.GATTToolBackend()
adapter.start()

addr = 'D0:F0:18:43:F2:B7'
uuit = '04710c43-4c62-4de8-9c1b-c439689d1886'

while True:  
 try:
    device = adapter.connect('00:38:40:0A:00:04', 5)
    break
 except pygatt.exceptions.NotConnectedError:
    print('Waiting...')


#device.subscribe('0002021-0000-1000-8000-00805f9b34fb', callback = printIndication, indication = True)
#device.subscribe('00002022-0000-1000-8000-00805f9b34fb', callback = printIndication, indication = True)
#device.subscribe('00002a19-0000-1000-8000-00805f9b34fb', callback = printIndication, indication = True)


device.disconnect()
adapter.stop()