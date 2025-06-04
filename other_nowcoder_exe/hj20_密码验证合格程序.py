import sys
lines = [] # 空列表接收输入的密码
while True:
    line = input()
    if line == "": #如果是空行就终止
        break
    lines.append(line)

def character(pw): # 定义字符验证函数
    count = 0 #初始化字符种类
    for i in pw:
        ascii_code = ord(i) # 获取字符的ASCII码
        if 48 <= ascii_code <= 57: # 数字
            count += 1 #包含数字类字符
            

def verify(pw): # 定义验证函数
    if len(pw) < 8: # 长度小于8就不合格
        print("NG")
