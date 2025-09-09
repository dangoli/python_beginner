s = input()
s1 = input()
result = "" # 底串
for char in s:
    if char not in result:
        result += char
s26 = "abcdefghijklmnopqrstuvwxyz"
for char in s26:
    if char not in result:
        result += char
output = ""
list_res = list(result) # 底串转列表
for char in s1:
    xvhao = ord(char) -97 
    output += list_res[xvhao]

print(output)