def array_two(lst): # 返回二维数组的函数
    lst_2 = []
    for item in lst:
        s1 = list(item)
        temp = s1
        lst_2.append(temp)
    return lst_2

def array_sort(lst): # 按ASCII排序函数
    pass

def dic_sort(lst):
    pass

n = int(input())
lst = []
for i in range(n):
    s = input()
    temp = s
    lst.append(temp)
# array2 = array_two(lst)
# print(array2)

lst.sort(key=None, reverse=False)
for item in lst:
    print(item)