s = input() #
x, y = 0, 0
for cmd in s.split(';'): #cmd是str类
    if not cmd: #如果cmd为空则跳过
        continue
    if len(cmd) not in [2, 3]: #如果cmd的长度不是2或3则跳过
        continue
    direc = cmd[0] #direc接受指令的方向
    if direc not in ['W', 'A', 'S', 'D']: #如果direc不是WASD则跳过
        continue
    num = cmd[1:] #num接受指令的步数
    if not num.isdigit(): #如果num不是数字则跳过
        continue
    inum = int(num) 
    if not (0 < inum < 100):
        continue
    if direc == 'A':
        x -= inum
    elif direc == 'D':
        x += inum
    elif direc == 'W':
        y += inum
    elif direc == 'S':
        y -= inum
print(f'{x},{y}') #输出坐标