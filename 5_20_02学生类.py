class Student:
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score
    # 实例方法
    def info(self):
        print(self.name, self.age, self.gender, self.score)

print('请输入5位学生信息:(姓名#年龄#性别#成绩)')
lst = []
for i in range(1, 6):
    s = input(f'请输入第{i}位学生信息:')
    s_lst = s.split('#') # 将输入的字符串转换为列表
    # 创建学生对象
    stu = Student(s_lst[0], int(s_lst[1]), s_lst[2], int(s_lst[3]))
    # 将学生对象添加到列表中
    lst.append(stu)

# 输出学生信息
for item in lst:
    item.info()