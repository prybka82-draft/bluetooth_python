from __future__ import print_function
import logging

# https://gist.github.com/peplin/f765ae283cc695999560d350659a322b

logging.basicConfig()
logging.getLogger('pygatt').setLevel(logging.INFO)

import binascii
import pygatt

import os
import sys

ADDRESS = "D0:F0:18:43:F2:B7"
# Many devices, e.g. Fitbit, use random addressing - this is required to connect.
ADDRESS_TYPE = pygatt.BLEAddressType.random

address = ADDRESS

hci = "hci0"

if os.environ['BACKEND'] == "gatttool":
    adapter = pygatt.GATTToolBackend(hci_device=hci)
else:
    adapter = pygatt.BGAPIBackend()

adapter.start()

devices = adapter.scan(run_as_root=True, timeout=3)

for device in devices:
    address = device['address']

    try:
        print("Connecting...")
        device = adapter.connect(address, address_type=ADDRESS_TYPE)
        print("Connected")

        for uuid in device.discover_characteristics().keys():

            print("\n\nChecking uuid: {}\n".format(uuid))

            try:
                print("Reading characteristics")
                val = device.char_read(uuid)
                print("Characterisic read. Printing raw walue: {}".format(val))
                print("Read UUID %s: %s" % (uuid, binascii.hexlify(device.char_read(uuid))))

            except Exception as e:
                print("EXCEPTION: {}".format(e))
                continue
            else:
                break
        device.disconnect()
    except pygatt.exceptions.NotConnectedError:
        print("failed to connect to %s" % address)
        continue
    else:
        break
else:
    print("failed to connect and read from any device")
    sys.exit(1)