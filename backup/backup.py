#!/usr/bin/env python3

"""
A program to backup from one or more source directories (local or external)
to a designated "backup" external drive.

* external drives *may* have a "drive ID" file
* use rsync to copy along with it's nice "link" feature
* perform optional filesystem check on source or target drives
* backup to timestamped directories on target drive
* config data in ~/.backup (or ./.backup) config file
"""

import config as cfg

# name of the config file
ConfigFile = '.backup.cfg'


def backup():
    cfg_filepath = cfg.find_config(ConfigFile)
    if cfg_filepath is None:
        raise RuntimeError(f"Can't find config file '{ConfigFile}'")
    config = cfg.get_config(cfg_filepath)
    result = config.test.test
    print(f'config.test.test={result}')
    print(f'config.test2.test2={config.test2.test2}')
    print(cfg.list_config(config))
#    check_source_mounted(config)
#    check_target_mounted(config)

backup()
