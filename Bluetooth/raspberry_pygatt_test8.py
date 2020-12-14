from __future__ import print_function
import logging, binascii, pygatt, os, sys

# https://gist.github.com/peplin/f765ae283cc695999560d350659a322b
# listowanie charakterystyk

logging.basicConfig()
logging.root.setLevel(logging.INFO)

address = "D0:F0:18:43:F2:B7"
hci = "hci0"

adapter = pygatt.GATTToolBackend(hci_device=hci)
adapter.start()

devices = adapter.scan(run_as_root=True, timeout=3)
iNode = adapter.connect(address)

characteristics = iNode.discover_characteristics()

for char in characteristics.keys():
    print("uuid: {}, handle: {}".format(char, hex(characteristics[char].handle)))


iNode.disconnect()



