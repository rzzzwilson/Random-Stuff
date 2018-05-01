#!/usr/bin/env python3

"""
Implement a circular buffer.  Use global variables (BAD!).
"""

maxsize = 5

queue = []
for _ in range(maxsize):
    queue.append(None)
rear = 0
front = 0

def enqueue(new_item):
    global front, rear
    if front >= rear:
        size = front - rear
    else:
        size = rear - front

    if size == maxsize - 1:
        print ('Queue is full.')
    else:
        queue[front] = new_item
        front += 1
        if front >= maxsize:
            front = 0

def dequeue():
    global front, rear
    if rear == front:
        print('Queue is empty.')
    else:
        result = queue[rear]
        rear += 1
        if rear >= maxsize:
            rear = 0
        return result

print(f'Start: rear={rear}, front={front}, queue={queue}')
enqueue("bag")
print(f'after "bag": rear={rear}, front={front}, queue={queue}')
enqueue("bag2")
print(f'after "bag2": rear={rear}, front={front}, queue={queue}')
enqueue("bag3")
print(f'after "bag3": rear={rear}, front={front}, queue={queue}')
enqueue("bag4")
print(f'after "bag4": rear={rear}, front={front}, queue={queue}')
enqueue("bag5")
print(f'after "bag5": rear={rear}, front={front}, queue={queue}')
result = dequeue()
print(f'after dequeue(): rear={rear}, front={front}, queue={queue}')
print(f'result={result}')
enqueue("bag6")
print(f'after "bag6": rear={rear}, front={front}, queue={queue}')
result = dequeue()
print(f'after dequeue(): rear={rear}, front={front}, queue={queue}')
print(f'result={result}')
result = dequeue()
print(f'after dequeue(): rear={rear}, front={front}, queue={queue}')
print(f'result={result}')
