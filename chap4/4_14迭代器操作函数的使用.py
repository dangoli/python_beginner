lst = [54, 56, 77, 4, 567, 34]
#(1)排序操作
asc_lst = sorted(lst)
desc_lst = sorted(lst, reverse=True)
print('原列表：', lst)
print('升序：', asc_lst)
print('降序：', desc_lst)

#(2)反向 reversd
new_lst = reversed(lst)
print(type(new_lst)) # <class 'list_reverseiterator'>
print(list(new_lst))

#(3)zip
x = ['a', 'b', 'c', 'd']
y = [10, 20, 30, 40, 50]
zipobj = zip(x, y)
print(type(zipobj)) # <class 'zip'>
# print(list(zipobj)) # [('a', 10), ('b', 20), ('c', 30), ('d', 40)]

#(4)enumerate 枚举
enum = enumerate(y, start=1)
print(type(enum)) # <class 'enumerate'>
print(tuple(enum)) # ((1, 10), (2, 20), (3, 30), (4, 40), (5, 50))

#(5)all
lst2 = [10, 20, '', 40]
print(all(lst)) # True
print(all(lst2)) # False

#(6)any
print(any(lst2)) # True

#(7)
print(next(zipobj))
print(next(zipobj))
print(next(zipobj))


def fun(num):
    return num%2 == 1 

obj = filter(fun, range(10)) # 将1-9都代入fun执行一次 保留结果为true的对象
print(list(obj))

def upper(x):
    return x.upper()

new_lst2 = ['hello', 'world', 'python']
obj2 = map(upper, new_lst2)
print(list(obj2))