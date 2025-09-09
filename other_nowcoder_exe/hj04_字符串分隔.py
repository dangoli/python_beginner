import sys

s = input() # input()函数返回str类
length = len(s)
s_add = '0'*(8-length%8)
print(s_add)
if(length%8 != 0):
    length = length + (8 - length%8) # length记录补0后长度

count = int(length/8)

new_s = s + s_add
s_lst = list(new_s)

for i in range(0, count):
    s_print = s_lst[0:8] # s_print列表
    str_print1 = ''.join(map(str,s_print))
    print(str_print1)
    del s_lst[0:8]