def array_two(lst): # 返回二维数组的函数
    lst_2 = []
    for item in lst:
        s1 = list(item)
        temp = s1
        lst_2.append(temp)
    return lst_2

n = int(input())
lst = []
for i in range(n):
    s = input()
    temp = s
    lst.append(temp)

# array2 = array_two(lst)
# array2.sort(key=None, reverse=False)
# print(array2)
lst.sort(key=None, reverse=False)
for item in lst:
    print(item)