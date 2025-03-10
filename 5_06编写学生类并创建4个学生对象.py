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

# 可创建多个对象
stu1 = Student('312', 22)
stu2 = Student('张三', 20)
stu3 = Student('李四', 17)
stu4 = Student('王五', 18)

print(type(stu1))

Student.school = 'SEU'

#将学生对象存储到列表中
lst = [stu1, stu2, stu3, stu4]
for item in lst:
    item.show() # 打点调用实例方法