#!user/bin/python3.6
# -*- coding=utf-8 -*-
# this is test
# 欢迎来到乾颐堂

import re
import os

ifconfig_result = 'eno33554944: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\n        inet 202.100.1.138  netmask 255.255.255.0  broadcast 202.100.1.255\n        inet6 fe80::20c:29ff:fe8d:5cb6  prefixlen 64  scopeid 0x20<link>\n        ether 00:0c:29:8d:5c:b6  txqueuelen 1000  (Ethernet)\n        RX packets 0  bytes 0 (0.0 B)\n        RX errors 0  dropped 0  overruns 0  frame 0\n        TX packets 33  bytes 4290 (4.1 KiB)\n        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\n\n'

ifconfig_findall_result = re.findall('([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})',ifconfig_result)

print('%s : %s' % ('MAC地址为',ifconfig_findall_result[0]))
print('MAC地址为 :',ifconfig_findall_result[0])

