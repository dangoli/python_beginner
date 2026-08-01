s = input()
length = len(s)
s_add = '0' * (8 - length % 8)
if length % 8 != 0:
    length = length + (8 - length % 8)

count = int(length/8)

new_s = s + s_add
s_lst = list(new_s)

for i in range(0, count):
    s_print = s_lst[0:8]
    str_print = ''.join(map(str, s_print))
    print(str_print)
    del s_lst[0:8]