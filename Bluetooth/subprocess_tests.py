import subprocess
import time

process = subprocess.Popen("ping gmail.com", stdout=subprocess.PIPE, encoding='utf-8')

time.sleep(10)

process.terminate()

out, err = process.communicate()

lines = str(out).split("\r\n")

for i in range(len(lines)):
    print("{}: {}".format(i, lines[i]))


#---------------------------------

# ok, ale trzeba jakoś zamknąć ten proces

# https://stackoverflow.com/questions/2502833/store-output-of-subprocess-popen-call-in-a-string
#res = subprocess.check_output("ping gmail.com")

#print("and the winner is: {}".format(res))

#result:
#and the winner is: b'\r\nPinging gmail.com [216.58.208.197] with 32 bytes of data:\r\nReply from 216.58.208.197: bytes=32 time=13ms TTL=118\r\nReply from 216.58.208.197: bytes=32 time=13ms TTL=118\r\nReply from 216.58.208.197: bytes=32 time=13ms TTL=118\r\nReply from 216.58.208.197: bytes=32 time=13ms TTL=118\r\n\r\nPing statistics 
#for 216.58.208.197:\r\n    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),\r\nApproximate round trip times in milli-seconds:\r\n    Minimum = 13ms, Maximum = 13ms, Average = 13ms\r\n'

#--------------------------

# process = subprocess.Popen("ping gmail.com")

# process.wait()

# res, err = process.communicate()

# print("and the winner is: {}".format(res))


#-------------------------

#res = subprocess.run(args=["ping gmail.com"], capture_output=True, encoding="utf-8", shell=True)

#time.sleep(10)

#res = res.stdout

#print("result: {}".format(res))

#time.sleep(2)

#print("result: {}".format(res))




