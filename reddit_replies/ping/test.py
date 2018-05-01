#!/usr/bin/env python

import subprocess
import multiprocessing
import Queue


nrange = '192.168.0.'
NumWorkers = 10


def ping_worker(adr_q, res_q, wnum):
    print('worker %d, starting' % wnum)
    while True:
        address = adr_q.get()
        adr_q.task_done()
        print('worker %d, address=%s' % (wnum, address))

        try:
            out = subprocess.check_output('ping -c 3 -W 3 %s' % address,
                                          stderr=subprocess.STDOUT, shell=True)
            res = 0
        except subprocess.CalledProcessError as e:
            out = e.output
            res = e.returncode
    
        if res == 0:
            result = '%13s (%02d): ping OK' % (address, wnum)
        elif res == 2:
            result = '%13s (%02d): no response' % (address, wnum)
        else:
            result = '%13s (%02d): ping failed for some reason, res=%d' % (address, wnum, res)

        print(result)
        res_q.put(result)

workers = []
address_q = Queue.Queue()
result_q = Queue.Queue()

for i in range(0, 255+1):
    address = nrange + str(i)
    address_q.put(address)
print('addresses generated')
print('address_q=%s' % type(address_q))
print('result_q=%s' % type(result_q))

for i in range(NumWorkers):
    p = multiprocessing.Process(target=ping_worker, args=(address_q, result_q, i))
    workers.append(p)
    p.start()
print('pool of %d workers started' % NumWorkers)

address_q.join()
#for p in workers:
#    p.join()
print('Finished, %d results (id(result_q)=%08x)' % (result_q.qsize(), id(result_q)))

while True:
    try:
        print(result_q.get_nowait())
        result_q.done()
    except Queue.Empty:
        break
