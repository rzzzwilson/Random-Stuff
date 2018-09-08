import stack_dump

def test():
    sd = stack_dump.StackDump('test.out')
    xc = stack_dump.StackDump('test2.out')

    sd('message')
    xc('message2')

if __name__ == '__main__':
    test()
