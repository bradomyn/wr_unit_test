#------------------------------
# generate and communicate between sockets
#
# function:
# socket_open:
# server = True  -> servermode
# server = False -> client mode
#
# socket_read:
# give 2 valued back, the message and the ip 
#
# python 2
# 11.2012
# zweig
#------------------------------
import socket

class socket_io:

	_mysocket = socket.socket()
	_ip   = 0    
	_port = 0     

	def socket_open(self, ip_target, port_target, server):
		
		try:
		  mysocket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
		except:
		  return False
	
		try:
		    if server:
		     mysocket.bind((ip_target, port_target))
		except:
		    return False

		socket_io._ip       = ip_target
		socket_io._port     = port_target
		socket_io._mysocket = mysocket 

		return True


	def socket_write(self, message):
		try:
		  socket_io._mysocket.sendto(message,(socket_io._ip,socket_io._port))		  
		  return True
		except:
		  return False


	def socket_read(self):
		try:
		  message,ip_sender = socket_io._mysocket.recvfrom(1024)
		  return (message, ip_sender, True)
		except:
		  return (message, ip_sender, False)

	def socket_close(mysocket):
		socket_io._mysocket.close()
