# def fun(n):
#     if n < 0:
#         return -1
#     elif n == 1:
#         return 1
#     else:
#         lst = [2, 8]
#         for i in range(1, n):
#             lst.append(lst[-1] + lst[-2])
#             return lst[-2]%lst[-1]
# print(fun(7))

# def fun(a, b):
#     s = pow(a, b)
#     return s
# print(fun(2, 5))

# lst = ['red', 'pink', 'blue']
# def fun(x):
#     lst.append(x)
# fun('white')
# print(lst)

# result = lambda x:10
# print(result(3))

# def fun(a = 1):
#     return a + 1
# print(fun(fun(fun())))

def fun():
    print('helloworld')
print(type(fun), type(fun()))