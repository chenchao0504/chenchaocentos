#!user/bin/python3.6
# -*- coding=utf-8 -*-
# this is test
# 欢迎来到乾颐堂

import re

str1 = '166     54a2.74f4.0326  DYNAMIC     Gi1/0/11'

str1_result = re.match('(\d{1,4})\s+([a-f0-9]{4}\.[a-f0-9]{4}\.[a-f0-9]{4})\s+(\w+)\s+(\w.*\d)',str1).groups()

print('-'*100)
print('%-15s : %s' % ('VLAN ID',str1_result[0]))
print('%-15s : %s' % ('MAC',str1_result[1]))
print('%-15s : %s' % ('Type',str1_result[2]))
print('%-15s : %s' % ('Interface',str1_result[3]))