import bluetooth
import sys

#za przykładem z:
#https://github.com/pybluez/pybluez/blob/master/examples/simple/sdp-browse.py

iNode = 'iNode-43F2B7'
#iNode = '/org/bluez/hci1/dev_D0_F0_18_43_F2_B7/service0011/char0012' #z charakterystyk wylistowanych programem bluetoothctl
#D0:F0:18:43:F2:B7
addr2 = r'/org/bluez/hci1/dev_D0_F0_18_43_F2_B7/service0011/char0012'

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee" #przykład z dokumentacji
uuid = "04710C43-4C62-4DE8-9C1B-C439689D1886".lower()

addr = 'D0:F0:18:43:F2:B7' #mac address (z charakterstyk wylistowanych programem bluetoothctl)

#sprawdzam możliwe adresy
a = addr # wyrzuca OSError:A
a = uuid # nic się nie dzieje - program urywa się po find_services, bez wyrzucenia błędu
a = addr2 # jw.

#services = bluetooth.find_service(address=a)

n = iNode # OSError: A
n = addr2 # OSError: A
n = uuid # OSError: A
n = addr # OSError: A

services = bluetooth.find_service(name=n)

if len(services) > 0:
    print(f'Found {len(services)} services')
else:
    print('No services found')

# błąd A
# spis numerów błędów: https://stackoverflow.com/questions/15304934/how-to-get-the-list-of-error-numbers-errno-for-an-exception-type-in-python
# jeśli A = 10
# błąd ECHILD: https://man7.org/linux/man-pages/man3/errno.3.html










