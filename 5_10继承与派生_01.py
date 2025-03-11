class BaseClassName:
    def __init__(self):
        self.a = 'aaaa'
        self.b = 'bbbb'
    def __action(self): # 基类的私有方法
        print('调用BaseClass的方法')

class DerivedClassName(BaseClassName):
    def __init__(self):
        super().__init__()
    # def action(self):
    #     super()._BaseClassName__action()
    #     print('派生类重写基类的方法')
    def add(self):
        return self.a + self.b

derived = DerivedClassName()
# derived.action() # 派生类调用自身的action方法而非基类的
print(derived.add()) # 
# 若派生类重写了基类的方法，想调用基类的方法，可使用super()

# 强调调用基类私有属性方法

# 调用基类的__init__方法

# 继承基类初始化过程中的参数
