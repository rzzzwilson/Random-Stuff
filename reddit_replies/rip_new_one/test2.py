!/usr/bin/env python

# This script requires shade, so you should pip install it before running this.
import sys

import shade
import os_client_config

# Uncomment and set this to True if you want to see the API calls
#shade.simple_logging(debug=True)

# This is instantiating a client.

def get_creds(cloud):
    try:
        return os_client_config.make_shade(cloud=cloud)
    except Exception as e:
        print e
        print "No %s cloud defined in clouds.yml or clouds.yml does not exist" % cloud
        sys.exit(1)

LABCREDS = get_creds('LAB')
EDCCREDS = get_creds('EDC')
PDCCREDS = get_creds('PDC')
SDCCREDS = get_creds('SDC')

# Functions

def get_owner(creds, server):

    try:
        metadata = creds.get_server(server).metadata[u'Owner']
        return metadata
    except:
        return "No Owner"

def get_service(creds, server):

    try:
        metadata = creds.get_server(server).metadata[u'Service']
        return metadata
    except:
        return "No Service"

def get_servers(creds):

    try:
        servers = creds.list_servers(all_projects=True)
        return servers
    except:
        return "No Server"

def get_flavor(creds, id):
    
    try:
        flavor = creds.get_flavor(id)
        return flavor.name
    except:
        return "No Flavor"

def get_project_name(creds, id):

    try:
        project = creds.get_project(id)
        return project.name
    except:
        return "No Project Name"

# Work work... get on with it!

print "Name, Instance ID, Service, Owner, Tenant, Region, Flavor, Root Disk"

for cred in (LABCREDS, EDCCREDS, PDCCREDS, SDCCREDS):
    servers = get_servers(cred)
    for s in servers:
        servernames = s[u'name']
        serverids = s[u'id']
        serverregion = s[u'region']
        servertenantid = s[u'project_id']
        flavorid = s[u'flavor'][u'id']
        serverrootdisk = s[u'properties'][u'OS-EXT-PF9-SRV-RES-INFO:res_info'][u'cfg_disk_gb']
    
        print "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}GB".format(servernames,
                                                    serverids,
                                                    get_service(cred, s),
                                                    get_owner(cred, s),
                                                    get_project_name(cred, servertenantid),
                                                    serverregion,
                                                    get_flavor(cred, flavorid),
                                                    serverrootdisk)
