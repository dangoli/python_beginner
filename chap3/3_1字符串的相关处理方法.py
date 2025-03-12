# 大小写转换
s1 = 'HelloWorld'
new_s2 = s1.lower()
print(s1, new_s2) # HelloWorld helloworld

new_s3 = s1.upper()
print(new_s3) # HELLOWORLD

# 字符串的分割
e_mail = 'leehan@163.com'
lst = e_mail.split('@') # 返回列表
print('邮箱名：', lst[0], '邮件服务器域名：', lst[1]) # 邮箱名： leehan 邮件服务器域名： 163.com

# 
print(s1.count('o'))  # 2 子串'o'在母字符串s1中出现了两次

# 检索操作
print(s1.find('o')) # 4 子串'o'在母字符串中第一次出现的位置
print(s1.find('p')) # -1 没有找到

print(s1.index('o')) # 4 子串'o'在母字符串中第一次出现的索引位置
# print(s1.index('p')) # ValueError: substring not found 子串未找到

# 判断前缀和后缀
print('demo.py'.endswith('.py')) # True
print('text.txt'.endswith('.txt')) # True
print(s1.startswith('H')) # True
print(s1.startswith('P')) # False