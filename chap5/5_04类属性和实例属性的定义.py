class Student:
    # 
    school = '北京XXX教育'

    # 初始方法
    def __init__(self, xm, age): # xm, age是方法的参数，是局部变量
        self.name = xm # =左侧是实例属性，xm是局部变量，
        self.age = age # 实例的名称可以和局部变量的名称相同