"""
Create a stack object from the python list.
"""

class stack(list):

    def __init__(self, *args, **kwargs):
        if args or kwargs:
            # for simplicity
            raise TypeError('Cannot create populated stack')
        super().__init__()

    def isEmpty(self):
        return len(self) == 0

    def peek(self):
        return self[-1]

    def push(self, obj):
        self.append(obj)

    def size(self):
        return len(self)
