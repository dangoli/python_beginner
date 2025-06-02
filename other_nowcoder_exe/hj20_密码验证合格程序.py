import sys
lines = [] # 空列表接收输入的密码
while True:
    line = input()
    if line == "": #如果是空行就终止
        break
    lines.append(line)

def verify(pw): # 定义验证函数
    if len(pw) < 8: # 长度小于8就不合格
        print("NG")
print(lines)