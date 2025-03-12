s1 = 'hello'
s2 = 'world'
# (1)使用+进行拼接
print(s1 + s2) # helloworld

# (2)使用字符串的join()方法
print(''.join([s1, s2])) # helloworld 使用空字符串进行拼接

print('*'.join(['hello', 'world', 'python', 'java', 'cpp'])) # hello*world*python*java*cpp
print('❤'.join(['hello', 'world', 'python', 'java', 'cpp'])) # hello❤world❤python❤java❤cpp

# (3)直接拼接 
print('hello''world') # helloworld

# (4)使用格式化字符串进行拼接
print('%s%s' % (s1, s2)) # 元组
print(f'{s1}{s2}')
print('{0}{1}'.format(s1, s2)) # helloworld
print('{1}{0}'.format(s1, s2)) # worldhello