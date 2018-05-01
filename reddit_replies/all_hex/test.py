#!/usr/bin/python3

def gen_all_hex():
     i = 0
     #while i < 16**8:
     while i < 16**5:
          yield "{:08X}".format(i)
          #yield format(i, "08X")
          #yield f'{i:08X}'
          i += 1

with open('data.txt', 'w') as fd:
    for hex_str in gen_all_hex():
        fd.write(hex_str + '\n')

