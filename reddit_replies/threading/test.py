"""
Sample code in reply to:
https://www.reddit.com/r/learnpython/comments/5onjhh/is_there_a_function_similar_to_interrupt/

Simple threading example.
"""

import sys
import time
from queue import Queue
import random
import threading

something = True
something_else = True

def do_one():
    print('do_one')

def do_two():
    print('do_two')

# this function runs in a separate thread
def thread_function(queue):
    """Randomly get a string and pass it back through queue.

    Note that this function has an infinite loop.
    """

    count = 0
    while True:
        count += 1
        time.sleep(0.1)
        if random.randrange(20) < 2:
            # only do this about 1 in 10 times
            queue.put(count)

def process(queue):
    """Loop calling the do_one() and do_two() functions.

    Also check the queue for items.
    """

    while True:
        # do anything you want here
        if something:
            do_one()
        if something_else:
            do_two()

        # check the queue and process item if something there
        while not queue.empty():
            item = queue.get()
            print('process: got %d' % item)
            queue.task_done()
        time.sleep(2.0)

queue = Queue()     # create the Queue object and pass it to thread
t = threading.Thread(target=thread_function, args=(queue,))
t.start()           # start the thread
process(queue)      # process
