# 创建一个空集合
s = set() # <class 'set'>
# 录入5位朋友的姓名和手机号
for i in range(1, 6):
    info = input(f'请输入第{i}位好友的姓名和手机号：')
    # 添加到集合中
    s.add(info)
# 遍历集合
for lee in s:
    print(lee)