# s1 = True
# s2 = True
# s3 = True
# s4 = False
# lst = [s1, s2, s3]
# lst2 = [s1, s2, s4]

# def bool_lst(lst):
#     len_f = len(lst)
#     i = 0
#     for item in lst:
#         if item:
#             i += 1
#     if i == len_f:
#         return True
#     else:
#         return False

# bool_lsts = bool_lst(lst) #
# bool_lst2 = bool_lst(lst2)
# print(bool_lsts)
# print(bool_lst2)

# lst = [180]
# for item in lst:
#     lst.pop(item)

# f = False
# lst_flag = list()
# for i in range(2):
#     lst_flag.append(f)

# print(lst_flag) 

lst = [1,1,1,1,1,2,2,3,3,5]

print(" ".join(str(i) for i in lst))