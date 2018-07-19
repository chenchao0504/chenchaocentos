import re
str1 = """TCP Student  192.168.189.167:32806 Teacher  137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO 
TCP Student  192.168.189.167:80 Teacher  137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO """

str1_result = str1.split('\n')
dict1 = {}
list1 = []
list2 = []
for i in str1_result:
    str1_list_result = re.match('.*\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s+.*\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*\s+bytes\s+(\d+).*flags\s+(\w+)\s*',i).groups()
    print(str1_list_result)
    qyt_key = str1_list_result[0],str1_list_result[1],str1_list_result[2],str1_list_result[3]
    qyt_value = str1_list_result[4],str1_list_result[5]
    dict1[qyt_key] = qyt_value
    list1.append(str1_list_result)
    list2.extend(str1_list_result)

print('\n\n打印字典\n\n')
print(dict1)


print('\n\n格式化打印输出\n\n')
for key,value in dict1.items():
    print(key, value)
    print('%10s : %-20s | %10s : %-10s | %10s : %-10s | %10s : %-10s |' %('src',key[0],'src_p',key[1],'dst',key[2],'dst_p',key[3]))
    print('%10s : %-20s | %10s : %-10s' %('bytes',value[0],'flags',value[1]))


print(list1)
for x in list1:
    print(x)
    print('%10s : %-20s | %10s : %-10s | %10s : %-10s | %10s : %-10s |' % ('src', x[0], 'src_p', x[1], 'dst', x[2], 'dst_p', x[3]))
    print('%10s : %-20s | %10s : %-10s' % ('bytes', x[0], 'flags', x[1]))

print(list2)
print('%10s : %-20s | %10s : %-10s | %10s : %-10s | %10s : %-10s |' % ('src', list2[0], 'src_p', list2[1], 'dst', list2[2], 'dst_p', list2[3]))
print('%10s : %-20s | %10s : %-10s' % ('bytes', list2[4], 'flags', list2[5]))
print('%10s : %-20s | %10s : %-10s | %10s : %-10s | %10s : %-10s |' % ('src', list2[-6], 'src_p', list2[-5], 'dst', list2[-4], 'dst_p', list2[-3]))
print('%10s : %-20s | %10s : %-10s' % ('bytes', list2[-2], 'flags', list2[-1]))
