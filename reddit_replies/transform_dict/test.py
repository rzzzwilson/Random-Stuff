#!/bin/env python
# -*- coding: utf-8 -*-

"""
Instead of many 'if' statements.

From: https://www.reddit.com/r/learnpython/comments/6stcof/is_there_a_way_to_shorten_this_if_statement_mess/
"""

transform_dict = {'person1': 'another name',
                  'person2': 'a name',
                  'person3': 'yet another name'
                 }

x = 'person2'
x = transform_dict.get(x, 'unknown name')
