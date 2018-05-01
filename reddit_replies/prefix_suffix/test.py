#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Code playing with the problem from:

https://www.reddit.com/r/learnpython/comments/6hr3o7/match_partial_strings_without_hardcoding_pattern/
"""

from collections import defaultdict

Data = """PEX VI (ESPN)
PEX VI (Shallowhill)
PEX VI (ON)
UTAR
MEZZ and Proctor
South east Distressed OFF
South east Distressed ON
South east Distressed MGR"""

ps_dict = defaultdict(list)

for line in Data.split('\n'):   # loop over every line in input data
    try:
        (prefix, suffix) = line.rsplit(sep=' ', maxsplit=1)
    except ValueError:
        # only one word in line
        prefix = line
        suffix = None
    ps_dict[prefix].append(suffix)

for (key, value) in ps_dict.items():
    if value == [None]:
        print('%s' % key)
    else:
        print('%s %s' % (key, ' '.join(value)))
