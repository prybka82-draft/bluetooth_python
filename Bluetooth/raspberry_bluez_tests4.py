import bluetooth
import sys
import time

#za przykładem z:
#https://github.com/pybluez/pybluez/blob/master/examples/simple/sdp-browse.py

iNode = 'iNode-43F2B7'
#iNode = '/org/bluez/hci1/dev_D0_F0_18_43_F2_B7/service0011/char0012' #z charakterystyk wylistowanych programem bluetoothctl
#D0:F0:18:43:F2:B7
addr2 = r'/org/bluez/hci1/dev_D0_F0_18_43_F2_B7/service0011/char0012'

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee" #przykład z dokumentacji
uuid = "04710C43-4C62-4DE8-9C1B-C439689D1886".lower()

addr = 'D0:F0:18:43:F2:B7' #mac address (z charakterstyk wylistowanych programem bluetoothctl)

serverMACAddress = addr
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))



s.close()






