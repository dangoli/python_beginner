n = input() # input()函数返回str类
s = list(n) #转成一维列表 s=['9', '8', '7', '6', '6', '7', '3']
s.reverse() # 不会产生新的列表，在原列表基础上进行 ['3', '7', '6', '6', '7', '8', '9']
s_o = []
for i in range(len(s)):
    if s[i] in s_o:
        pass
    else:
        temp = s[i]
        s_o.append(temp)
n_str = "".join(s_o)
print(n_str)