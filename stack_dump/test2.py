"""
See if multiple imports work correctly.
"""

import stack_dump
import test

sd2 = stack_dump.StackDump('test.out')
xc2 = stack_dump.StackDump('test2.out')

test.test()

sd2('message')
xc2('message2')
