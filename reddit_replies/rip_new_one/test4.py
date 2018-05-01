#!/usr/bin/env python3
import sys
import shade
import os_client_config

Clouds = ('LAB', 'EDC', 'PDC', 'SDC')

def get_creds(cloud_list):
    """Return list containing the credentials for all clouds in 'cloud_list'."""

    result = []
    for cloud in cloud_list:
        try:
            result.append(os_client_config.make_shade(cloud=cloud))
        except Exception as e:  # need more specific exception catch
            print(e)
            print(f'No {cloud} cloud defined in clouds.yml or clouds.yml does not exist')
            sys.exit(1)
    return result

def get_owner(creds, server):
    try:
        return creds.get_server(server).metadata[u'Owner']
    except:     # need to catch explicit exception, not just a "catch all"
        return "No Owner"

def get_service(creds, server):
    try:
        return creds.get_server(server).metadata[u'Service']
    except:     # ditto
        return "No Service"

def get_servers(creds):
    try:
        return creds.list_servers(all_projects=True)
    except:     # ditto
        return None

def get_flavor(creds, ident):
    try:
        return creds.get_flavor(ident).name
    except:     # ditto
        return "No Flavor"

def get_project_name(creds, ident):
    try:
        return creds.get_project(ident).name
    except:     # ditto
        return "No Project Name"


for cred in get_creds(Clouds):
    print('Name, Instance ID, Service, Owner, Tenant, Region, Flavor, Root Disk')
    servers = get_servers(cred)
    if servers:
        for s in servers:
            servernames = s[u'name']
            serverids = s[u'id']
            serverregion = s[u'region']
            servertenantid = s[u'project_id']
            flavorid = s[u'flavor'][u'id']
            serverrootdisk = s[u'properties'][u'OS-EXT-PF9-SRV-RES-INFO:res_info'][u'cfg_disk_gb']
            print(f'{servernames}, {serverids}, {get_service(cred, s)}, '
                  f'{get_owner(cred, s)}, {get_project_name(cred, servertenantid)}, '
                  f'{serverregion}, {get_flavor(cred, flavorid)}, '
                  f'{serverrootdisk}GB')
    else:
        print("No servers")
