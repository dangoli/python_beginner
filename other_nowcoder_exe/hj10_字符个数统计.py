s = input() 
lst_s = list(s)
lst_asc = [] # 存储字符串中字符的ASCII码
for item in lst_s:
    asc_s = ord(item)
    temp = asc_s
    lst_asc.append(temp)
set_asc = set(lst_asc) # 转集合
print(len(set_asc))