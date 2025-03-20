import sys
# 字符串 哈希

s = input('输入一串字符').strip() # 输入字符串 保证首位不是空格
print(s)
# c = input('输入待查询的字母or数字')
# ord_c = ord(c)
# print(ord_c)
flag = 1
while(flag):
    c = input('输入待查询的字母or数字，只能输入字母或数字')
    c_len = len(c)
    if c_len == 1:
        ord_c = ord(c)
        if (ord_c >= 48 and ord_c <= 57) or (ord_c >= 65 and ord_c <= 90) or (ord_c >= 97 and ord_c <= 122):
            flag = 0
    else:
        flag = 1


s_lower = s.lower()
c_lower = c.lower()
count = 0
for t in s_lower:
    if t == c_lower:
        count += 1

print(f'%s中有%d个%s'%(s_lower,count,c_lower))