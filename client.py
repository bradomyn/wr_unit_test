import socket
import time
import os
import subprocess

ANY = "0.0.0.0"
MCAST_ADDR = "224.168.2.9"
MCAST_PORT = 1600

def empty(data):
    print "No action for this sms ID"

def execute(data):
    print "We should execute sth here"
    path=os.path.join(os.path.dirname(__file__),'test')
    dir_list = os.listdir(path)

    for fname in dir_list:
        script = "./"+path+"/"+fname
        print script
        subprocess.call(script)
    
    
#create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#allow multiple sockets to use the same PORT number
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#Bind to the port that we know will receive multicast data
sock.bind((ANY,MCAST_PORT))
#tell the kernel that we are a multicast socket
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
#Tell the kernel that we want to add ourselves to a multicast group
#The address for the multicast group is the third param
status = sock.setsockopt(socket.IPPROTO_IP,
socket.IP_ADD_MEMBERSHIP,
socket.inet_aton(MCAST_ADDR) + socket.inet_aton(ANY));

sock.setblocking(0)
ts = time.time()
while 1:
    try:
        data, addr = sock.recvfrom(1024)
    except socket.error, e:
        pass
    else:
        print "Incoming Packet"
        print "FROM: ", addr
        print "DATA: ", data
        print data[0:4]

        filter= { ('0x01') in data: empty, 
                  ('0x02') in data: empty,
                  ('0x03') in data: empty,
                  ('0x04') in data: execute}[1]    

# it will filter the packets and decides what to do
# according to the msg id
        filter(data)


