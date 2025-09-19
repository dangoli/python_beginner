def statistic():
    n_1, n_2, n_3, n_4 = 0, 0, 0, 0 # 分别代表字母、数字、空格、其他字符的个数
    s = input()
    for ch in s:
        ascii_value = ord(ch) # 获取字符的ASCII值
        if 65 <= ascii_value <=90 or 97 <= ascii_value <= 122: # 字母
            n_1 += 1
        elif 48 <= ascii_value <= 57: # 数字
            n_2 += 1
        elif ascii_value == 32: # 空格
            n_3 += 1
        else:
            n_4 += 1
    return n_1, n_2, n_3, n_4

if __name__ == "__main__":
    n_1, n_2, n_3, n_4 = statistic()
    print(n_1)
    print(n_3)
    print(n_2)
    print(n_4)