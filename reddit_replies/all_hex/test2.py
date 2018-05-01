#!/usr/bin/python3

import itertools

hex_list = '0123456789ABCDEF'

with open('data.txt', 'w') as fd:
    for hex_0 in hex_list:
        for hex_1 in hex_list:
            for hex_2 in hex_list:
                for hex_3 in hex_list:
                    for hex_4 in hex_list:
                        for hex_5 in hex_list:
                            for hex_6 in hex_list:
                                for hex_7 in hex_list:
                                    fd.write(f'{hex_0}{hex_1}{hex_2}{hex_3}{hex_4}{hex_5}{hex_6}{hex_7}\n')

