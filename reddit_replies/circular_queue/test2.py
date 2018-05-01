#!/usr/bin/env python3

"""
Implement a circular buffer.  Use a state object (GOOD!).
"""

maxsize = 5

queue = []
for _ in range(maxsize):
    queue.append(None)
rear = 0
front = 0

def make_queue(max_size):
    """Make a 'queue' object.

    Actually a list: [queue_list, front, rear, max_size]
    """

    queue = []
    for _ in range(maxsize):
        queue.append(None)
    rear = 0
    front = 0
    return [queue, front, rear, maxsize]

def enqueue(queue, new_item):
    if queue[1] >= queue[2]:
        size = queue[1] - queue[2]
    else:
        size = queue[2] - queue[1]

    if size == queue[3] - 1:
        print ('Queue is full.')
    else:
        queue[0][queue[1]] = new_item
        queue[1] += 1
        if queue[1] >= maxsize:
            queue[1] = 0

def dequeue(queue):
    if queue[2] == queue[1]:
        print('Queue is empty.')
    else:
        result = queue[0][queue[2]]
        queue[2] += 1
        if queue[2] >= queue[3]:
            queue[2] = 0
        return result

def print_queue(msg, queue):
    print(f'{msg}: rear={queue[2]}, front={queue[1]}, queue={queue[0]}')

queue = make_queue(5)
print_queue('Start', queue)
enqueue(queue, "bag")
print_queue('after "bag"', queue)
enqueue(queue, "bag2")
print_queue('after "bag2"', queue)
enqueue(queue, "bag3")
print_queue('after "bag3"', queue)
enqueue(queue, "bag4")
print_queue('after "bag4"', queue)
enqueue(queue, "bag5")
print_queue('after "bag5"', queue)
result = dequeue(queue)
print_queue('after dequeue()', queue)
print(f'result={result}')
enqueue(queue, "bag6")
print_queue('after "bag6"', queue)
result = dequeue(queue)
print_queue('after dequeue()', queue)
print(f'result={result}')
result = dequeue(queue)
print_queue('after dequeue()', queue)
print(f'result={result}')
