#!user/bin/python3.6
# -*- coding=utf-8 -*-
# this is test
# 欢迎来到乾颐堂

import re
str1 = 'Port-channel1.189   192.168.189.254     YES     CONFIG      up'

str1_result = re.match('(\w+.*)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w+)\s+(\w+)\s+(\w+)',str1).groups()

print('%-10s : %-s' %('接口',str1_result[0]))
print('%-10s : %-s' %('IP地址',str1_result[1]))
print('%-10s : %-s' %('状态',str1_result[2]))
