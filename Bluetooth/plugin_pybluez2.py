import bluetooth, sys, logging

logging.basicConfig()
logging.root.setLevel(logging.INFO)

# lookign for devices and services

logging.info("Discovering devices")
devices = bluetooth.discover_devices(duration=10, lookup_names=True, flush_cache=True, lookup_class=False)
logging.info(f"Found {len(devices)} devices")

logging.info("Printing addresses and names")
for addr, name in devices:
    print(f"\t{addr} - {name}")

uuid = "04710c43-4c62-4de8-9c1b-c439689d1886"
addr = "D0:F0:18:43:F2:B7" #nie widzi tego adresu, nie potrafi się podłączyć

# services = bluetooth.find_service(uuid=uuid, address=addr)

# if len(services) == 0:
#     print(f"No servieces found")
#     sys.exit(0)
# else:
#     print(f"Found {len(services)} services")