from __future__ import print_function
import time, sys, logging, logging.handlers
from bgapi.module import BlueGigaModule, GATTCharacteristic, GATTService, BlueGigaClient, BlueGigaServer
from bgapi.cmd_def import gap_discover_mode, gap_connectable_mode

SERVER_SERIAL = "COM7"

if __name__ == "__main__":    
    ble_server = BlueGigaServer(port=SERVER_SERIAL, baud=115200, timeout=1)
    #error: could not open port COM7