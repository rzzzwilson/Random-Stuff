import subprocess, os, threading, time
from queue import Queue
from socket import inet_aton
import struct

_start = time.time()
hosts = []

def check(n):
    with open(os.devnull, "wb") as limbo:
        ip = "192.168.0.{0}".format(n)
        result = subprocess.Popen(["ping", "-c", "1", "-W", "700", ip], stdout=limbo, stderr=limbo).wait()
        if not result:
            hosts.append(ip)

def threader():
    while True:
        worker = q.get()
        check(worker)
        q.task_done()


q = Queue()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
for worker in range(1, 255):
    q.put(worker)
q.join()

hosts = sorted(hosts, key=lambda ip: struct.unpack("!L", inet_aton(ip))[0])
print('\n'.join(str(p) for p in hosts))
print(len(hosts), " hosts up")
print("Process completed in: ", time.time() - _start)
