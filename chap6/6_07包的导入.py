import admin.my_admin as a
a.info()

print('-' * 20)
from admin import my_admin as b
b.info()

print('-' * 20)
from admin.my_admin import info # 导入模块中的函数
info()

from admin.my_admin import * # 导入模块中的所有函数
print(name)