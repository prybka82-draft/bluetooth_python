from lightblue import *

# https://sourceforge.net/projects/lightblue/files/lightblue/0.4/lightblue-0.4_s60-3rdEd-FP1_PyS60-1.9.x.zip/download?use_mirror=master&download=
# pip install python-lightblue

devices = lightblue.finddevices() # lightbue is not defined

for dev in devices:
	print(dev)
	services = lightblue.findservices(dev[0])
	for s in services:
		print(s)
	print()
	print()





