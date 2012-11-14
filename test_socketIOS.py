import sys
import time
from socket_io import socket_io

target 	 = '140.181.86.124'
port   	 = 5005

def connectASserver():

	message = " "
	ip_sender = ' '

	server = socket_io()
	status = server.socket_open(target, port, True)
	if not status:
	  print "* Fail open socket *"
	  end()

	message, ip_sender, status = server.socket_read() 

	if not status:
	  print "* Error during reading *"
	  end()

	print "reading ", message, " from ", ip_sender

	server.socket_close()


def connectASclient():

	message= "this is a fuking testmessage"

	client = socket_io()
	status = client.socket_open(target, port, False)
	if not status:
	  print "* Fail open socket *"
	  end()

	status = client.socket_write(message)
	
	if not status:
	  print "* Fail send message*"
	  end()

	client.socket_close()



def end():
	sys.exit('shit, some errors here....')



connectASserver()


