!/usr/bin/env python

# This script requires shade, so you should pip install it before running this.
import sys

import shade
import os_client_config

# Uncomment and set this to True if you want to see the API calls
#shade.simple_logging(debug=True)

# This is instantiating a client.

try:
    LABCREDS = os_client_config.make_shade(cloud="LAB")
except Exception as e:
    print e
    print "No LAB cloud defined in clouds.yml or clouds.yml does not exist."
    sys.exit(1)

try:
    EDCCREDS = os_client_config.make_shade(cloud="EDC")
except Exception as e:
    print e
    print "No EDC cloud defined in clouds.yml or clouds.yml does not exist."
    sys.exit(1)

try:
    PDCCREDS = os_client_config.make_shade(cloud="PDC")
except Exception as e:
    print e
    print "No PDC cloud defined in clouds.yml or clouds.yml does not exist."
    sys.exit(1)

try:
    SDCCREDS = os_client_config.make_shade(cloud="SDC")
except Exception as e:
    print e
    print "No SDC cloud defined in clouds.yml or clouds.yml does not exist."
    sys.exit(1)

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

servers = get_servers(LABCREDS)
for s in servers:
    servernames = s[u'name']
    serverids = s[u'id']
    serverregion = s[u'region']
    servertenantid = s[u'project_id']
    flavorid = s[u'flavor'][u'id']
    serverrootdisk = s[u'properties'][u'OS-EXT-PF9-SRV-RES-INFO:res_info'][u'cfg_disk_gb']

    print "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}GB".format(servernames,
                                                serverids,
                                                get_service(LABCREDS, s),
                                                get_owner(LABCREDS, s),
                                                get_project_name(LABCREDS, servertenantid),
                                                serverregion,
                                                get_flavor(LABCREDS, flavorid),
                                                serverrootdisk)

print "Name, Instance ID, Service, Owner, Tenant, Region, Flavor, Root Disk"

servers = get_servers(EDCCREDS)
for s in servers:
    servernames = s[u'name']
    serverids = s[u'id']
    serverregion = s[u'region']
    servertenantid = s[u'project_id']
    flavorid = s[u'flavor'][u'id']
    serverrootdisk = s[u'properties'][u'OS-EXT-PF9-SRV-RES-INFO:res_info'][u'cfg_disk_gb']

    print "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}GB".format(servernames,
                                                serverids,
                                                get_service(EDCCREDS, s),
                                                get_owner(EDCCREDS, s),
                                                get_project_name(EDCCREDS, servertenantid),
                                                serverregion,
                                                get_flavor(EDCCREDS, flavorid),
                                                serverrootdisk)

print "Name, Instance ID, Service, Owner, Tenant, Region, Flavor, Root Disk"

servers = get_servers(PDCCREDS)
for s in servers:
    servernames = s[u'name']
    serverids = s[u'id']
    serverregion = s[u'region']
    servertenantid = s[u'project_id']
    flavorid = s[u'flavor'][u'id']
    serverrootdisk = s[u'properties'][u'OS-EXT-PF9-SRV-RES-INFO:res_info'][u'cfg_disk_gb']

    print "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}GB".format(servernames,
                                                serverids,
                                                get_service(PDCCREDS, s),
                                                get_owner(PDCCREDS, s),
                                                get_project_name(PDCCREDS, servertenantid),
                                                serverregion,
                                                get_flavor(PDCCREDS, flavorid),
                                                serverrootdisk)

print "Name, Instance ID, Service, Owner, Tenant, Region, Flavor, Root Disk"

servers = get_servers(SDCCREDS)
for s in servers:
    servernames = s[u'name']
    serverids = s[u'id']
    serverregion = s[u'region']
    servertenantid = s[u'project_id']
    flavorid = s[u'flavor'][u'id']
    serverrootdisk = s[u'properties'][u'OS-EXT-PF9-SRV-RES-INFO:res_info'][u'cfg_disk_gb']

    print "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}GB".format(servernames,
                                                serverids,
                                                get_service(SDCCREDS, s),
                                                get_owner(SDCCREDS, s),
                                                get_project_name(SDCCREDS, servertenantid),
                                                serverregion,
                                                get_flavor(SDCCREDS, flavorid),
                                                serverrootdisk)
                                                