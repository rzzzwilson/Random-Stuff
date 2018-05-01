#!/usr/bin/env python3

"""
Implement a circular buffer.  Use a class (GOOD!).
"""

class CircularQueue:
    def __init__(self, maxsize=5):
        self.maxsize = maxsize
        self.queue = []
        for _ in range(maxsize):
            self.queue.append(None)
        self.rear = 0
        self.front = 0

    def enqueue(self, new_item):
        if self.front >= self.rear:
            size = self.front - self.rear
        else:
            size = self.rear - self.front
    
        if size == self.maxsize - 1:
            print ('Queue is full.')
        else:
            self.queue[self.front] = new_item
            self.front += 1
            if self.front >= self.maxsize:
                self.front = 0

    def dequeue(self):
        if self.rear == self.front:
            print('Queue is empty.')
        else:
            result = self.queue[self.rear]
            self.rear += 1
            if self.rear >= self.maxsize:
                self.rear = 0
            return result

    def string(self, msg):
         return f'{msg}: rear={self.rear}, front={self.front}, queue={self.queue}'

queue = CircularQueue(5)
print(queue.string('Start'))
queue.enqueue("bag")
print(queue.string('after "bag"'))
queue.enqueue("bag2")
print(queue.string('after "bag2"'))
queue.enqueue("bag3")
print(queue.string('after "bag3"'))
queue.enqueue("bag4")
print(queue.string('after "bag4"'))
queue.enqueue("bag5")
print(queue.string('after "bag5"'))
result = queue.dequeue()
print(queue.string('after dequeue()'))
print(f'result={result}')
queue.enqueue("bag6")
print(queue.string('after "bag6"'))
result = queue.dequeue()
print(queue.string('after dequeue()'))
print(f'result={result}')
result = queue.dequeue()
print(queue.string('after dequeue()'))
print(f'result={result}')
