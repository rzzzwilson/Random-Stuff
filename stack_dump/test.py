import stack_dump

#sd = stack_dump.StackDump([1, 2, 3])
sd = stack_dump.StackDump('test.out')
#fd = open('test.out', 'r')
#sd = stack_dump.StackDump(fd)

sd('message')
sd('message2')
