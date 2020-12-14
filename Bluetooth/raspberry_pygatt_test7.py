from __future__ import print_function
import logging,binascii,pygatt,os,sys,time
from uuid import *


def handle_data(handle, value):
    #print("{}".format(value))
    print("this is data handler")


logging.basicConfig()
logging.root.setLevel(logging.INFO)

address = "D0:F0:18:43:F2:B7"
hci = "hci0"

logging.info("Creating adapter")
adapter = pygatt.GATTToolBackend(hci_device=hci)
#adapter = pygatt.BGAPIBackend() #brakuje serial_port
logging.info("Adapter created\n")

logging.info("Starting adapter")
time.sleep(5)
adapter.start()
logging.info("Adapter started\n")

device = None

try:
    # laczenie z czujnikiem
    logging.info("Connecting to {}".format(address))
    time.sleep(5)
    #device = adapter.connect(address,timeout=10,auto_reconnect=True)
    device = adapter.connect(address,timeout=10)
    logging.info("Connected\n")

    # ustawianie trybu pracy
    uuid="04710c43-4c62-4de8-9c1b-c439689d1886"
    value=bytearray(b'\xA0\x00') #czestotliwosc 3,25 Hz, zmienna i stala akcelerometru, kazda probka z akc. i magn.

    logging.info("Setting work mode in {} as {}".format(uuid, value))
    time.sleep(5)
    device.char_write(uuid=uuid,value=value,wait_for_response=True)
    logging.info("Work mode set\n")

    logging.info("Reading characteristic from {}".format(uuid))
    res = device.char_read(uuid)
    logging.info("Value read: {}\n".format(res))

    # wlaczanie notyfikacji

    handle = 0x2902 #no response received
    #handle = 0x60e4 #timeout exception
    #handle = 0x7444 #timeout exception
    #uuid = UUID(hex='0x2902') #badly formed hexadecimal uuid
    uuid = "00001801-0000-1000-8000-00805f9b34fb" #no characteristic found
    uuid = "0000cb4a-5efd-45be-b5be-158df376d8ad" #jw
    uuid = "0000cb4d-5efd-45be-b5be-158df376d8ad" #wpisuje sie, notyfikacja nie dziala
    uuid = "00002901-0000-1000-8000-00805f9b34fb" #no characteristic found
    uuid = "00002902-0000-1000-8000-00805f9b34fb" #jw
    uuid = "0000cb4c-5efd-45be-b5be-158df376d8ad" #wpisuje sie, notyfikacja nie dziala
    uuid = "00002901-0000-1000-8000-00805f9b34fb" #no characteristic found
    uuid = "04710c44-c624-de89-c1bc-4396089d1886" #jw
    uuid = "04710c43-4c62-4de8-9c1b-c439689d1886" #wpisuje sie, notyfikacja nie dziala
    uuid = "00002901-0000-1000-8000-00805f9b34fb" #no characteristic found
    uuid = "00002902-0000-1000-8000-00805f9b34fb" #jw
    uuid = "04710c44-4c62-4de8-9c1b-c439689d1886" #wpisuje sie, notyfikacja nie dziala
    uuid = "a477e473-94df-4e22-a81b-cf8a6748898c" #no characteristic found
    uuid = "a477e474-94df-4e22-a81b-cf8a6748898c" #wpisuje sie, notyfikacja nie dziala
    uuid = "a477e475-94df-4e22-a81b-cf8a6748898c" #no responce received
    uuid = "a477e476-94df-4e22-a81b-cf8a6748898c" #wpisuje sie, notyfikacja nie dziala
    uuid = "9b4820ee-d114-4dab-a25e-cc0122b3d64d" #no characteristic found
    uuid = "9b4821ee-d114-4dab-a25e-cc0122b3d64d" #wpisuje sie, notyfikacja nie dziala
    uuid = "00002901-0000-1000-8000-00805f9b34fb" #no characteristic found
    uuid = "0000180a-0000-1000-8000-00805f9b34fb" #jw
    uuid = "00002a24-0000-1000-8000-00805f9b34fb" #no response received, poza tym opisana jako Model Number String
    uuid = "00002a27-0000-1000-8000-00805f9b34fb" #no response received, poza tym opisana jako Hardware Revision String
    uuid = "00002a26-0000-1000-8000-00805f9b34fb" #no response received, poza tym opisana jako Firmware Revision String
    uuid = "00002a28-0000-1000-8000-00805f9b34fb" #no response received, poza tym opisana jako Software Revision String
    uuid = "00002a29-0000-1000-8000-00805f9b34fb" #no response reveived, poza tym opisana jako Manufacturer Name String
    uuid = "00001804-0000-1000-8000-00805f9b34fb" #no characteristic found
    uuid = "00002a07-0000-1000-8000-00805f9b34fb" #wpisuje sie, notyfikacja nie dziala

    value=bytearray(b'\x01\x00')
    #logging.info("Setting notification mode using handle {} and value {}".format(handle, value))
    #device.char_write_handle(handle=handle,value=value,wait_for_response=True)
    #device.char_write(uuid,value=value,wait_for_response=True)
    #logging.info("Notification turned on")

    #uuid="04710c44-4c62-4de8-9c1b-c439689d1886"
    #handle = 0x5240
    #logging.info("Reading characteristic from uuid {}".format(uuid))
    #res = device.char_read(uuid) #sczytuje 01 08, nie reaguje na zmiane polozenia czujnika
    #res = device.char_read_long(uuid) #wywala nieokreslony exception
    #res = device.char_read_handle(10) #cos sie sczytuje, ale co
    #res = device.char_read_handle(handle,timeout=5) #wywala timeout exception
    #logging.info("Value read: {}\n".format(res))

    # subskrybowanie

    uuid = "04710c43-4c62-4de8-9c1b-c439689d1886" #subskrybuje sie do tego uuid, ale nie pojawiaja sie notyfikacje
    #uuid = "04710c44-c624-de89-c1bc-4396089d1886" #no characteristic found
    logging.info("Subscribing to uuid {}".format(uuid))
    time.sleep(5) #w internetach komus pomoglo odczekanie paru sekund
    #device.bond()
    device.subscribe(uuid, callback=handle_data, indication=True)
    logging.info("Subscribed")
    #time.sleep(5)

    while 1:
        pass

except pygatt.exceptions.NotConnectedError as e:
    logging.error("Pygat's not connected exception: {}".format(e))
except pygatt.exceptions.NotificationTimeout as e:
    logging.error("Pygat's notification timeout exception: {}".format(e))
except Exception as e:
    logging.error("Some other exception: {}".format(e))
finally:
    logging.info("Disconnecting device")
    if device != None:
        device.disconnect()
    logging.info("Device disconnected")

logging.info("Exiting program")





