from bluetooth.ble import DiscoveryService

service = DiscoveryService()
devices = service.discover(2)


for address, name in devices.items():
    print(f"Name: {name}, add: {address}")

