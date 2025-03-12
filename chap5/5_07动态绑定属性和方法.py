class Student:
    # 
    school = '北京XXX教育'

    # 初始化方法
    def __init__(self, xm, age): # xm, age是方法的参数，是局部变量
        self.name = xm # =左侧是实例属性，xm是局部变量，
        self.age = age # 实例的名称可以和局部变量的名称相同
    
    # 定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'我叫:{self.name}, 今年:{self.age}岁了')


stu1 = Student('312大人', 22)
stu2 = Student('张三', 17)
print(stu1.name, stu1.age)
print(stu2.name, stu2.age)

# 为stu2动态绑定一个实例属性
stu2.gender = 'male'
print(stu2.name, stu2.age, stu2.gender)

# print(stu1.name, stu1.age, stu1.gender) # AttributeError: 'Student' object has no attribute 'gender'
# 动态绑定方法
def introduce():
    print('我困死了，我是一个普通的函数，被动态绑定成了stu2对象的方法')
stu2.fun = introduce # 函数的赋值
# fun就是stu2对象的方法
# 调用
stu2.fun()