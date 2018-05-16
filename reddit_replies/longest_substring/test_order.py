import time
from test import longest_sequence

test_string = 'abcdefghijklmnopqrstuvwxyz'

lengths = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]

for l in lengths:
    # create string 'l' instances of 'test_string'
    big_string = ""
    for _ in range(l):
        big_string += test_string

    # time calling longest_sequence() on 'big_string'
    start = time.time()
    result = longest_sequence(big_string)
    delta = time.time() - start
    print(f"l={l:03d}, size={len(big_string)}, delta={delta}, s/1000={delta/len(big_string)}")
