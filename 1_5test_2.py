# 模拟10086查询话费
answer = 'y'
while answer == 'y':
    print('----------------欢迎使用10086话费查询系统----------------')
    print('1.查询当前余额')
    print('2.查询当前的剩余流量')
    print('3.查询当前的剩余通话时长')
    print('0.退出系统')
    choice = input('请输入您的操作：')
    if choice == '1':
        print('当前余额为234.5元')
    elif choice == '2':
        print('当前剩余流量为4GB')
    elif choice == '3':
        print('当前剩余通话时长为320分钟')
    elif choice == '0':
        print('系统关闭，感谢您的使用！')
        break
    else:
        print('对不起，您输入有误，请重新输入')
    answer = input('是否继续使用系统？y/n')
else:
    print('系统关闭，感谢您的使用！')