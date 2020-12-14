import bluetooth 
import select
import sys
import time

devices = bluetooth.discover_devices(lookup_names=True)

#pybluez
#stary plugin jeszcze dla pythona 2
#dla pythona 3 wymaga wersji 3.1 (z nowszymi nie działa)
# python setup.py install
# instalator setup.py wymaga Microsoft Visual C++ 14.0 or greater
# inny sposób instalacji
# python setup.py install

# https://stackoverflow.com/questions/21000680/how-to-find-visible-bluetooth-devices-in-python
# https://github.com/pybluez/pybluez
# https://github.com/pybluez/pybluez/blob/master/docs/install.rst
# https://github.com/pybluez/pybluez/blob/master/examples/simple/rfcomm-server.py
# http://www.robertprice.co.uk/robblog/programming_bluetooth_using_python-shtml/

devices = bluetooth.discover_devices(lookup_names=True)

for addr, name in devices:

    print(addr, name)

    try:
        services = bluetooth.find_service(name, address=addr)

        for i in services:
            print(i)

    except: 
        print("couldn't find service")
    print()
    time.sleep(5)

# 34:88:5D:D0:3C:29 None
# couldn't find service

# 64:1C:B0:F3:1F:D5 None
# couldn't find service

# C8:69:CD:56:E0:F5 None
# couldn't find service

# 24:FC:E5:F9:D8:C3 None
# couldn't find service





#simple inquiry example

nearby_devices = bluetooth.discover_devices(lookup_names=True, duration=8)
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
     print("  {} - {}".format(addr, name))
     time.sleep(5)

addr = "24:FC:E5:F9:D8:C3"

print("--------------------------------")

# read local bluetooth device address

print(f"Local bluetooth device address: {bluetooth.read_local_bdaddr()}")

print("--------------------------------")

print("looking for nearby devices...")

nearby_devices = bluetooth.discover_devices(lookup_names = True, duration = 20, flush_cache = True)

for addr, name in nearby_devices:
    print(f"\n----------\naddres: {addr}\nnames: {name}")

    try:
        for service in bluetooth.find_service(address = addr):  # find_service nie działa
            print("name: {}".format(service['name']))
            print("description: {}".format(service['description']))
            print("protocol: {}".format(service['protocol']))
            print("provider: {}".format(service['provider']))
            print("port: {}".format(service['port']))
            print("service id: {}".format(service['service-id']))
            print("\n\n")
    except Exception as e:
        print(f"exception occurred: {e}")

#---------------------------------

print("----------------------------")
print("----------------------------")

devices = bluetooth.bt.discover_devices(duration=10, flush_cache=True)

for device in devices:
    print(device)

print("----------------------------")
print("----------------------------")

# wyszukanie usługi o nrze 0x04710C44C624DE89C1BC4396089D1886

import uuid

t = 0x04710C44C624DE89C1BC4396089D1886

#u = uuid.UUID(int=t)

#service = bluetooth.find_service(uuid=0x04710C44C624DE89C1BC4396089D1886) #invalid uuid
#service = bluetooth.find_service(uuid=uuid.UUID(int=0x04710C44C624DE89C1BC4396089D1886)) #invalid uuid
#service = bluetooth.find_service(uuid=uuid.UUID(hex=0x04710C44C624DE89C1BC4396089D1886)) #int object has no attribute replace


print("----------------------------")
print("----------------------------")


