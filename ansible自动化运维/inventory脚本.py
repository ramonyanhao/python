#!/usr/bin/env python

import sys

try:

    import json

except ImportError:

    import simplejson as json


def RFile():
    with open('hostlist.txt', 'r+') as f:

        result = []

        for line in f.readlines():  # line='ramon 192.168.43.129'

            host = line.strip().split()  # host=['ramon','192.168.43.129'],通过strip()移除line中的空字符,再通过split把str转为列表

            if host:
                result.append(host)

    return result


host_list = RFile()  # host_list结果是[['ramon','192.168.43.129']]


def groupList():
    group_list = []

    for host in host_list:
        group_list.append(host[1])

    print(json.dumps({"all": group_list}, indent=4))


def hostList(key):
    host_dict = {}

    for host in host_list:
        host_dict[host[1]] = {"ansible_ssh_host": host[1],  "ansible_ssh_user": "sshuser",
                              "ansible_ssh_pass":

                                  "sshuser", "hostname": host[0]}

    print(json.dumps(host_dict[key], indent=4))


if len(sys.argv) == 2 and (sys.argv[1] == '--list'):

    groupList()

elif len(sys.argv) == 3 and (sys.argv[1] == '--host'):

    hostList(sys.argv[2])

else:

    print("Usage: %s --list or --host <hostname>" % sys.argv[0])

    sys.exit(1)