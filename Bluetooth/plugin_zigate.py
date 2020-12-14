import logging
import zigate

#https://pypi.org/project/zigate/

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)
logging.

z = zigate.connect(port=None)

version = z.get_version_text()
print(version)

z.get_devices_list()

devices = z.devices
print(devices) #ZiGate has not been found...


