#rx all signals and compute action and send to arduino

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
	
	#start threads
	lThreadA = startThreads(setupListenSocket(port, "1001"), listenThread())
	lThreadB = startThreads(setupListenSocket(port, "1002"), listenThread())
	lThreadC = startThreads(setupListenSocket(port, "1003"), listenThread())
	lThreadD = startThreads(setupListenSocket(port, "1004"), listenThread())
	
	#setup Timers
	startTime = now = startTimeDisp = time.time()
	dispTimeout = 1
	timeout = 5
	
	#run the program
	while(now - startTime) <= timeout:
		if now-startTimeDisp >= dispTimeout:
			print lThreadA, lThreadB, lThreadC, lThreadD
			startTimeDisp = now
			
		now = time.time()
	
	#end threads
	lThreadA.join()
	lThreadB.join()
	lThreadC.join()
	lThreadD.join()
	sys.exit()
