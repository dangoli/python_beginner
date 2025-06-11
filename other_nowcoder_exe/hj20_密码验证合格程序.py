import sys

def character(pw) -> bool: # 定义字符验证函数
    flag = [0, 0, 0, 0]
    for i in pw:
        ascii_code = ord(i) # 获取字符的ASCII码
        if 48 <= ascii_code <= 57: # 数字
            flag[2] = 1 #包含数字类字符
        elif 65 <= ascii_code <= 90: # 大写字母
            flag[0] = 1
        elif 97 <= ascii_code <= 122: # 小写字母
            flag[1] = 1
        elif 33 <= ascii_code <= 47 or 58 <= ascii_code <= 64 or 91 <= ascii_code <= 96 or 123 <= ascii_code <= 126: # 特殊字符
            flag[3] = 1
    if sum(flag) < 3: # 如果不包含三种类型的字符就不合格
        return False
    else:
        return True
            
def identical(pw: str) -> bool: # 定义重复子串验证函数
    n = len(pw)
    max_l = n // 2 # 最长子串长度
    for l in range(3, max_l + 1):
        first_occur = {} # 字典记录子串第一次出现的位置
        for i in range(0, n - l + 1):
            sub = pw[i:i + l] # 当前子串
            if sub not in first_occur: # 如果子串第一次出现
                first_occur[sub] = i # 记录子串首次出现位置1
            else:
                j = first_occur[sub] # 如果子串已经出现过
                if j + l <= i: # 如果子串不重叠
                    return False # 存在不重叠的重复子串
    return True # 没有不重叠的重复子串


def len_verify(pw) -> bool: # 定义验证函数
    if len(pw) < 8: # 长度小于8就不合格
        return False
    else:
        return True
    
while True:
    try:
        pw = input()
        result_len = len_verify(pw) 
        result_character = character(pw)
        result_identical = identical(pw) # 验证重复子串
        if result_len and result_character and result_identical:
            print('OK')
        else:
            print('NG')
    except:
        break