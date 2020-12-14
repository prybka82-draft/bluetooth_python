import bluetooth
import sys

#za przykładem z:
#https://github.com/pybluez/pybluez/blob/master/examples/simple/rfcomm-client.py

iNode = 'iNode-43F2B7'
#iNode = '/org/bluez/hci1/dev_D0_F0_18_43_F2_B7/service0011/char0012' #z charakterystyk wylistowanych programem bluetoothctl
#D0:F0:18:43:F2:B7

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee" #przykład z dokumentacji
uuid = "04710C43-4C62-4DE8-9C1B-C439689D1886".lower()

addr = 'D0:F0:18:43:F2:B7' #mac address (z charakterstyk wylistowanych programem bluetoothctl)

try:
    services = bluetooth.find_service(address=addr)

    if len(services) == 0:
        print("No services found")
    else:
        service = services[0]
        name = service['name']

        print(name)
except OSError as e:
    print('\nan exception was caught:')
    print(f'{e}')
    print(f'--->{sys.exc_info()[0]}')
    print(f'--->{e.__class__}')
    print(f'--->{e.args[0]}')
    print(f'\n\n')
    print(f'{OSError.__doc__}')

print("it is done")


#-------------------

# socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# socket.bind(("", bluetooth.PORT_ANY))
# socket.listen(1)

# port = socket.getsockname()[1]

#---------------

# devs = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

# for addr, name in devs:
#     try:
#         print(name)
#     except UnicodeEncodeError:
#         print('error')



