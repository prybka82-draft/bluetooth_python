import socket

#http://blog.kevindoran.co/bluetooth-programming-with-python-3/

serverMACAddress = 'D0:F0:18:43:F2:B7'

port = 3

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

#s.connect((serverMACAddress,port)) #TimeoutError: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond

# while 1:
#     text = input()
#     if text == "quit":
#         break
#     s.send(bytes(text, 'UTF-8'))

# s.close()

#----------

hostMACAddress = 'D0:F0:18:43:F2:B7'
backlog = 1
size = 1024

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

s.bind((hostMACAddress,port)) #OSError: [WinError 10049] The requested address is not valid in its context
s.listen(backlog)

try:
    client, address = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data)
except:	
    print("Closing socket")	
    client.close()
    s.close()







