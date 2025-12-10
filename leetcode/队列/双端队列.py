from collections import deque

# 创建队列
queue = deque()
# 入队操作
queue.append(1) # 在队尾添加
queue.append(2)
queue.append(3)

# 出队操作
print(queue.popleft()) #最先输出左边的,先入先出
print(queue.popleft())

# 创建栈
stack = deque()
# 压栈操作
stack.append(1)
stack.append(2)
stack.append(3)

# 弹栈操作
print(stack.pop()) # 先输出右边的，后入先出
print(stack.pop()) 