#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A 'global' module that allows attributes to be set/modified and
can have a persistant form on disk.
"""

import json as _json


# we must exclude the 'singleton' scaffolding names
# anythriong not using a lxieading underscore
_Exclude = []


def _payload():
    """Get a dict of the 'payload' attributes."""

    result = {}

    for (k, v) in globals().items():
        if not k.startswith('_') and k not in _Exclude:
            result[k] = v

    return result

def _save(filename=__name__+'.state'):
    """Save the singleton attributes in the given file."""

    save_data = _payload()

    json_str = _json.dumps(save_data, sort_keys=True, indent=4)

    with open(filename, 'w') as fd:
        fd.write(json_str + '\n')

def _load(filename=__name__+'.state'):
    """Load the singleton state from the given filename."""

    try:
        with open(filename, 'r') as fd:
            data = _json.load(fd)
    except FileNotFoundError:
        return

    globals_dict = globals()
    for (k, v) in data.items():
        globals_dict[k] = v
