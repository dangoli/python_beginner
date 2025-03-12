class Instrument: # 乐器类 基类
    def play(self):
        pass

class Erhu(Instrument): # 二胡类
    def play(self):
        print('二胡在演奏...')

class Piano(Instrument): # 钢琴类
    def play(self):
        print('钢琴在演奏...')

class Violin(Instrument): # 小提琴类
    def play(self):
        print('小提琴在演奏...')

# 编写一个演奏乐器的函数
def play(obj):
    obj.play()

# 创建乐器对象
erhu = Erhu()
piano = Piano()
violin = Violin()

# 调用函数
play(erhu)
play(piano)
play(violin)
