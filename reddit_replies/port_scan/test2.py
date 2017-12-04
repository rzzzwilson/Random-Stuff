import sys
import socket
from datetime import datetime
import Queue
import threading

NumWorkers = 250

def thread_port_check(requestq, resultq):
    while True:
        try:
            port = requestq.get(block=False)
        except Queue.Empty:
            break

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            resultq.put("Port {}:  Open".format(port))
        sock.close()

# Ask for input
remoteServer = raw_input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

# Check what time the scan started
t1 = datetime.now()

# create thread list and request/result Queues
threads = []
requestq = Queue.Queue()
resultq = Queue.Queue()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)
for port in range(1, 1024+1):
    requestq.put(port)

# start workers in the thread pool
for worker in range(NumWorkers):  
    t = threading.Thread(target=thread_port_check, args=(requestq, resultq))
    threads.append(t)
    t.start()

# wait until all threads are finished
for t in threads:
    t.join()

while not resultq.empty():
    print(resultq.get())

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
