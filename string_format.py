#!user/bin/python3.6
# -*- coding=utf-8 -*-
# this is test
# 欢迎来到乾颐堂

Department1 = 'Security'
Department2 = 'Python'
Manager1 = 'cq_bomb'
Manager2 = 'qinke'
COURSE_FEES1 = 25000
COURSE_FEES2 = 30000

# line1 = 'Department1 name:%-15s  Manager:%-15s  COUSE FFES:%-10d  The End!' % (Department1,Manager1,COURSE_FEES1)
# line2 = 'Department2 name:%-15s  Manager:%-15s  COUSE FEES:%-10d  The End!' % (Department2,Manager2,COURSE_FEES2)

line1 = 'Department1 name:{0:<15}  Manager:{1:<15}  COUSE FEES:{2:<10} The End!'.format(Department1,Manager1,COURSE_FEES1)
line2 = 'Departmetn2 name:{0:<15}  Manager:{1:<15}  COUSE FEES:{2:<10} The End!'.format(Department2,Manager2,COURSE_FEES2)

print('='*100)
print(line1)
print(line2)
print('='*100)