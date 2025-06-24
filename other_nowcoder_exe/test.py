def is_palindrome(s):
    # 去除首尾空格，并将字符串转为小写
    s = s.strip().lower()
    # 判断字符串是否等于其反转
    return s == s[::-1]

'''
str = input("请输入一个字符串: ")
if is_palindrome(str):
    print("是回文字符串")
else:
    print("不是回文字符串")
'''