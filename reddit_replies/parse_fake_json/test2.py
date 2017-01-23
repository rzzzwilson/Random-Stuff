#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://www.reddit.com/r/learnpython/comments/5plfhb/beginner_need_help_parsing_json/

Take 2.
"""

# the test data
Data = "[{u'id': 234207492300014L, u'name': u'General:'}, {u'id': 141253567024793L, u'name': u'Misc'}]"
print('Data=%s' % Data)

# just eval the whole shebang
eval_data = eval(Data)

# dump each dictionary
for d in eval_data:
    print('\tid=%s' % d['id'])
    print('\tname=%s' % d['name'])
