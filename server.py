import socket
import time
import os

#ANY = "192.168.1.1"
ANY = socket.gethostbyname(socket.gethostname())
print ANY
SENDERPORT = 1501
MCAST_ADDR = "224.168.2.9"
MCAST_PORT = 1600


#path, it should be from the conf fie or defult path

path=os.path.join(os.path.dirname(__file__), 'test')

#read the content of the 
dirList = os.listdir(path)

for fname in dirList:
        print fname


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

#The sender is bound on (0.0.0.0:1501)
sock.bind((ANY,SENDERPORT))

#Tell the kernel that we want to multicast and that the data is sent
#to everyone (255 is the level of multicasting)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)

while 1:
    time.sleep(1)
#Any subscribers to the multicast address will receive this data
    sock.sendto("0x04_1_2_5_P_7", (MCAST_ADDR,MCAST_PORT) );


