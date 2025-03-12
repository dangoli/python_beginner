class BaseClassName:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def dev(self):
        return self.a - self.b
    
# 
class DerivedClassName(BaseClassName):
    def __init__(self, a, b, c = 17): # 派生类增加参数c默认为17
        BaseClassName.__init__(self, a, b)
        self.c = c
    def add(self):
        return self.a + self.b
    def compare(self):
        if self.c > (self.a + self.b):
            return True
        else:
            return False

derived = DerivedClassName(2, 3)
print(derived.dev()) # 调用基类的dev函数
print(derived.add()) # 调用自身的add函数
print(derived.compare())
