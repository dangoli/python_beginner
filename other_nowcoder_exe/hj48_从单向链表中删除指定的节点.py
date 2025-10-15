"""
定义一种单向链表的构造方法如下:
-先输入一个整数n, 代表链表中节点总数.
-再输入一个整数h, 代表头节点的值;
-此后输入n-1个二元组(a, b), 代表在b的节点后插入值为a的节点
除此之外, 保证输入的链表中不存在重复的节点值.
现在, 对于给定的链表构造方法, 和一个额外的整数k, 你需要先按照上述的构造方法构造出链表, 随后删除值为k 的节点, 输出剩余链表.
输入描述:
在一行上:
1. 先输入一个整数n(1到1000之间)代表链表中节点的总数;
2. 再输入一个整数h代表头节点的值;
3. 此后输入n-1个二元组(a, b), 代表在b的节点后插入值为a的节点,(在1到10000之间);
4. 最后输入一个整数k(1到10000之间), 代表要删除的节点的值.
除此之外, 保证每个b的值在输入前已经存在于链表中; 每个a值在输入前均不存在于链表中. 节点的值各不相同.
输出描述:
在一行上输出n-1个整数, 代表删除指定元素后剩余的链表.
"""

inputs = list(map(int, input().split()))
n = inputs[0]
h = inputs[1]
pairs = inputs[2:-1]
k = inputs[-1]

# 构造链表, key为节点值, value为下一个节点值
nexts = {} #用字典保存每个节点的下一个节点值
order = [h]
for i in range(0, len(pairs), 2):
    a, b = pairs[i], pairs[i + 1]
    # 在b后插入a
    nexts[a] = nexts.get(b, None)
    nexts[b] = a

# 删除值为k的节点
res = []
cur = h
while cur is not None:
    if cur != k:
        res.append(cur)
    cur = nexts.get(cur, None)

print(' '.join(map(str, res)))