import bluetooth

print("Performing inquiry...")

#nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True,
#                                            flush_cache=True, lookup_class=False)

nearby_devices = bluetooth.discover_devices(duration=10)

print("Found {} devices".format(len(nearby_devices)))

for addr in nearby_devices:
    try:
        print("   {}".format(addr))
    except UnicodeEncodeError:
        print("   {}".format(addr))