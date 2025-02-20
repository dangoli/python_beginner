s = 'helloworldhelloworldhelloworldwhdjssidhdjdsuu'
# (1)字符串拼接及not in
new_s = ''
for item in s:
    if item not in new_s:
        new_s += item # 拼接操作
print(new_s) # helowrdjsiu


# (2)使用索引＋not in 
new_s2 = ''


