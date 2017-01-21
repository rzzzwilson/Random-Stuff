#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test the singleton module.
"""

import singleton

def test2(value):
    singleton.test2 = value
    print('test2: singleton/harry=%s' % str(singleton.harry))
