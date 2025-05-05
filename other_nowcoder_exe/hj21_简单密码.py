def transletter(a): # 对参数 字符进行转换
    asc_a = ord(a)
    if asc_a == 97 or asc_a == 98 or asc_a == 99:
        new_asc = 50
    elif asc_a == 100 or asc_a == 101 or asc_a == 102:
        new_asc = 51
    elif asc_a == 103 or asc_a == 104 or asc_a == 105:
        new_asc = 52
    elif asc_a == 106 or asc_a == 107 or asc_a == 108:
        new_asc = 53
    elif asc_a == 109 or asc_a == 110 or asc_a == 111:
        new_asc = 54
    elif asc_a == 112 or asc_a == 113 or asc_a == 114 or asc_a == 115:
        new_asc = 55
    elif asc_a == 116 or asc_a == 117 or asc_a == 118:
        new_asc = 56
    elif asc_a == 119 or asc_a == 120 or asc_a == 121 or asc_a == 122:
        new_asc = 57
    elif asc_a >= 65 and asc_a <= 89:
        new_asc = asc_a + 33
    elif asc_a == 90:
        new_asc = 97
    else:
        new_asc = asc_a
    return new_asc

s = input()
s_lst = list(s)
asc_lst = [] # 存储密码的ASCII码值
for item in s_lst:
    asc_le = transletter(item)
    temp = asc_le
    asc_lst.append(temp)
password = []
for item in asc_lst:
    pass_letter = chr(item)
    temp = pass_letter
    password.append(temp)
pss = ''.join(password)
print(pss)