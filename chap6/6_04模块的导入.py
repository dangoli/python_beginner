from my_info import *
from introduce import *
# 导入模块中具有相同的变量和函数，后导入的模块会覆盖前导入的模块
info()

import my_info
import introduce
my_info.info()
introduce.info()