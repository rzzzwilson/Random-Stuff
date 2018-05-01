from multiprocessing import Process, Queue
from Queue import Empty
import time

def f(q):
    q.put([42, None, 'hello'])
    time.sleep(1)
    q.put([43, None, 'processing'])
    time.sleep(0.5)
    q.put([44, None, 'processing'])
    time.sleep(1)
    q.put([45, None, 'processing'])
    time.sleep(1.5)
    q.put([46, None, 'bye'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    while p.is_alive() or not q.empty():
        if q.empty():
            time.sleep(0.25)
            continue
        result = q.get_nowait()

#        try:
#            result = q.get_nowait()
#        except Empty:
#            time.sleep(0.25)
#            continue

        print(str(result))
    p.join()    # probably not required in this simple case
