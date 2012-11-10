import socket
import time

ANY = "0.0.0.0"
MCAST_ADDR = "224.168.2.9"
MCAST_PORT = 1600

def empty_tex():
    print "No action for this sms ID"

def execute_tex():
    print data
    print "We should execute sth here"
    
# it will filter the packets and decides what to do
# according to the msg id

def msg_filter(msg_id):
    filter= {  msg_id == '0x01': empty(), 
            msg_id == '0x02': empty(),
            msd_id == '0x03': empty(),
            msd_id == '0x04': execute_tex(),
          }[msg_id]

    filter()

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
        msg_filter(data)
