#!user/bin/python3.6
# -*- coding=utf-8 -*-
# this is test
# 欢迎来到乾颐堂

import random

str1 = random.randint(1,255)
str2 = random.randint(0,255)
str3 = random.randint(0,255)
str4 = random.randint(1,255)

random_ip = str(str1) + '.' + str(str2) + '.' + str(str3) + '.' + str(str4)
print(random_ip)
