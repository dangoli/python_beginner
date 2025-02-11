# 
s = 'hello world'
s1 = s[0:5:2] #索引 从0开始，到5结束（不包含5）步长为2
print(s1) #hlo

# 省略了开始位置，默认为0
print(s[:5:2]) # hlo

#省略开始位置 省略步长默认为1
print(s[:5:]) # hello

#省略结束位置 默认为末尾 stop默认
print(s[::]) # hello world

# 省略开始与结束 只保留步长
print(s[::2]) #hlowrd

# 步长为负数
print(s[::-1]) # 逆序输出 dlrow olleh
print(s[-1:-12:-1])