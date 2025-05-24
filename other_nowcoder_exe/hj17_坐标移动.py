s = input().split(';') #list 指令分割在列表中
for cmd in s: #cmd是str类
    cmd = cmd.split() 
    if not cmd: #如果cmd为空则跳过
        continue
    if len(cmd) not in [2, 3]: #如果cmd的长度不是2或3则跳过
        continue
    direc = cmd[0] #direc接受指令的方向
    if direc not in ['W', 'A', 'S', 'D']: #如果direc不是WASD则跳过
        continue
    num = cmd[1:] #num接受指令的步数
    