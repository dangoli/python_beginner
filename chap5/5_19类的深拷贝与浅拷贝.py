class CPU():
    pass
class Disk():
    pass

class Computer():
    #
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


cpu = CPU()
disk = Disk()

com = Computer(cpu, disk)
# 变量(对象)的赋值
com1 = com # 浅拷贝 只是引用 两个变量指向同一个内存地址
print(com, '派生对象的内存地址:', com.cpu, com.disk)
print(com1, '派生对象的内存地址:', com1.cpu, com1.disk)
# print(com1)

# 类对象的浅拷贝
print('-' * 50)
import copy
com2 = copy.copy(com) # 浅拷贝 只是引用 两个变量指向同一个内存地址
print(com, '派生对象的内存地址:', com.cpu, com.disk)
print(com2, '派生对象的内存地址:', com2.cpu, com2.disk)

# 类对象的深拷贝
print('-' * 50)
com3 = copy.deepcopy(com) # 深拷贝 两个变量指向不同的内存地址
print(com, '派生对象的内存地址:', com.cpu, com.disk)
print(com3, '派生对象的内存地址:', com3.cpu, com3.disk)