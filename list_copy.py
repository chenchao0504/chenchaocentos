#!user/bin/python3.6
# -*- coding=utf-8 -*-
# this is test
# 欢迎来到乾颐堂

l1 = [2,5,9,7,8,3,1,6,4]

l2 = l1.copy()

l2.sort()

for i in range(len(l1)):
    print(l1[i],l2[i])
