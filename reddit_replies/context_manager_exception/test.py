#!/usr/bin/env python3

"""
Investigate raising an exception in a context manager __enter__() code.
"""

class TestCM():
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        if self.value < 5:
             raise Exception("Can't open CM")
        return self.value

    def __exit__(self, *args):
        pass

print('\nCM should work, return value 6')
with TestCM(6) as value:
    print(value)

print('\nCM should raise Exception that is caught')
try:
    with TestCM(3) as value:
        print(value)
except Exception as e:
    print(f"CM raised Exception, msg='{e}'")

print('\nCM should raise Exception')
with TestCM(3) as value:
    print(value)
