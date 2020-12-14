import pygatt

tv_address = "24:FC:E5:F9:D8:C3"
keyboard_address = "34:88:5D:D0:3C:29"

iNode_address = 0x04710C44C624DE89C1BC4396089D1886

#------------------------
#https://pypi.org/project/pygatt/


#adapter = pygatt.BGAPIBackend() #unable to auto-detect BLED112 serial port
#adapter = pygatt.BGAPIBackend(serial_port='COM9') #Unable to detect BLED112 serial port: COM9
#adapter = pygatt.GATTToolBackend() #requires BlueZ, which is not available in Windows

# wszystkie przykłady wymagają podania adresu w formacie 01:23:45:67:89:ab - ale nie ma metody wyszukującej urządzeń






