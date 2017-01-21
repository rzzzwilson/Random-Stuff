#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test the singleton module.
"""

import singleton

singleton.load()
payload = singleton.payload()
for (k, v) in payload.items():
    print('singleton.%s=%s\t%s' % (k, str(v), type(v)))

