s = input()
new_s = s.split() # 以空格分隔字符串 存储到列表里
new_s.reverse()
new_str = ' '.join(new_s)
print(new_str)