#recieves sensor messages and communicates messages
#transmits the efforts of the controller to the arduino



import zmq
import time
import threading
import sys
from sockets import *

			
if __name__ == "__main__":
	#subscribe setup
	port = "5556"
	socketA = setupListenSocket(port, "1001")
	socketB = setupListenSocket(port, "1002")
	
	#start threads
	lThreadA = startThreads(socketA, listenThread())
	lThreadB = startThreads(socketB, listenThread())
	
	#setup Timers
	startTime = now = startTimeDisp = time.time()
	dispTimeout = 1
	timeout = 5
	
	#run the program
	while(now - startTime) <= timeout:
		if now-startTimeDisp >= dispTimeout:
			print lThreadA, lThreadB
			startTimeDisp = now
			
		now = time.time()
	
	#end threads
	lThreadA.join()
	lThreadB.join()
	sys.exit()
