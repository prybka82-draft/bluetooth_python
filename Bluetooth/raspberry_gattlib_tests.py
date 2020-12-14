from gattlib import DiscoveryService

#https://pypi.org/project/gattlib/#discovering-devices


service = DiscoveryService("hci0")
devices = service.discover(2)

for address, name in devices.items():
    print("name: {}, address: {}".format(name, address))

#wymagana paczka gattlib
#pip install gattlib zwraca błąd: 
#OSError: Not supported OS