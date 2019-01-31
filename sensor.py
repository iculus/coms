#recieves commands from sensors and streams 
#transmits the efforts of the controller to the sensors

import zmq
import time 
import sys
from sockets import *
	
if __name__ == "__main__":
	#init messaging
	port = "5556"
	socketA = init(port)
	
	#setup Timers
	startTime = now = time.time()
	timeout = 5
	
	#run the program
	while(now - startTime) <= timeout:
	
		sendMessage(1001,45,socketA)
		sendMessage(1002,56,socketA)
		sendMessage(1003,67,socketA)
		sendMessage(1004,78,socketA)
		now = time.time()
		
	sys.exit()
	
