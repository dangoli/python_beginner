s = 'helloworldhelloworldhelloworldwhdjssidhdjdsuu' # str
# (1)字符串拼接及not in
new_s = ''
for item in s:
    if item not in new_s:
        new_s += item # 拼接操作
print(new_s) # helowrdjsiu


# (2)使用索引＋not in 
new_s2 = ''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2 += s[i]
print(new_s2)

# (3)通过集合去重+列表排序
print('-' * 32)
new_s3 = set(s) # set
lst = list(new_s3) # list
lst.sort(key=s.index) # 给列表排序
print(''.join(lst))