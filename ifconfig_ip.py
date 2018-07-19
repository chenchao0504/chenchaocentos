#!user/bin/python3.6
# -*- coding=utf-8 -*-
# this is test
# 欢迎来到乾颐堂

import os
import re
ifconfig_result = os.popen("ifconfig eth0").read()

re_findall_result = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)

for ip in re_findall_result:
    if ip.split('.')[-1] == '0':
        mask = ip
    elif ip.split('.')[-1] == '255':
        broadcast = ip
    else:
        ipv4 = ip

print('%15s : %-s' % ('Network mask',mask))
print('%15s : %-s' % ('Broadcast',broadcast))
print('%15s : %-s' % ('IPV4 Addr',ipv4))



