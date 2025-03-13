import my_info
print(my_info.name)
my_info.info()

import my_info as mi
print(mi.name)
mi.info()

# (2)from 模块名 import 函数名
from my_info import name # 只导入name 变量名称
print(name)


from my_info import info # 只导入info 函数
info()

# 通配符
from my_info import *

print(name)
info()

# 同时导入多个模块
import math, random, time