import socket # socket.engine
import sys

# http://blog.kevindoran.co/bluetooth-programming-with-python-3/
# https://docs.python.org/3.3/library/socket.html

# wykryte urzadzenia

#24:FC:E5:F9:D8:C3 None
#couldn't find service

#34:88:5D:D0:3C:29 None
#couldn't find service

#Found 2 devices.
#  34:88:5D:D0:3C:29 - Keyboard K380
#  24:FC:E5:F9:D8:C3 - [TV] Samsung 7 Series (50)
#--------------------------------
#Local bluetooth device address: ['A8:6D:AA:13:97:13']
#--------------------------------
#looking for nearby devices...

#----------
#addres: 34:88:5D:D0:3C:29
#names: Keyboard K380
#exception occurred: A

#----------
#addres: 24:FC:E5:F9:D8:C3
#names: [TV] Samsung 7 Series (50)
#exception occurred: A

tv_address = "24:FC:E5:F9:D8:C3"
keyboard_address = "34:88:5D:D0:3C:29"



# the public network interface
#HOST = socket.gethostbyname(socket.gethostname())
#print(f"host: {HOST}")

# create a raw socket and bind it to the public interface
#s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
#s.bind((HOST, 0))

# Include IP headers
#s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
#s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a package
#print(s.recvfrom(65565))

# disabled promiscuous mode
#s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

# https://stackoverflow.com/questions/36178389/python-socket-bluetooth - błąd socket nie ma właściwości AF_BLUETOOTH

# 24:FC:E5:F9:D8:C3 - [TV] Samsung 7 Series (50)

#baddr = '24:FC:E5:F9:D8:C3'
#channel = 4

#s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
#s.connect((baddr,channel))
#s_sock = server_sock.accept()

#print ("Accepted connection from "+address)

#data = s_sock.recv(1024)
#print ("received [%s]" % data)

#s.listen(1)

# http://blog.kevindoran.co/bluetooth-programming-with-python-3/

# serverMACAddress = tv_address
# port = 3
# s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) 

#s.connect((serverMACAddress,port))
# while 1:
#     text = input()
#     if text == "quit":
#         break
#     s.send(bytes(text, 'UTF-8'))
# s.close()





# HOST = ''
# PORT = 5007

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.listen(1) #invalid argument error

# conn,addr = s.accept()

# print('connected by: ', addr)

# while True:
#     data = conn.recv(1024)
#     if not data: break
#     conn.sendall(data)
# conn.close()




HOST = None
PORT = 5007

s = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    
    af, socktype, proto, cannonname, sa = res

    try:
        s = socket.socket(af, socktype, proto)
    except OSError as e:
        s = None
        continue

    try:
        s.bind(sa)
        s.listen(1)
    except OSError as e:
        s.close
        s = None
        continue

    break

if s is None:
    print('could not open socket')
    sys.exit(1)

conn,addr = s.accept()

print(f'connected by: {addr}')

while True:
    data = conn.recv(1024)

    if not data: break

    conn.send(data)

conn.close()






