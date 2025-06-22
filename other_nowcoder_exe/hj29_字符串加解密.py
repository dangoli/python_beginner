def encrypt(s: str) -> str: # 加密函数
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            # 小写字母变成大写 + 向后移一位
            if ch == 'z':
                result.append('A')
            else:
                result.append(chr(ord(ch.upper()) + 1))
        elif 'A' <= ch <= 'Z':
            # 大写字母变成小写 + 向后移一位
            if ch == 'Z':
                result.append('a')
            else:
                result.append(chr(ord(ch.lower()) + 1))
        elif '0' <= ch <= '9':
            # 数字+1，9→0
            result.append(str((int(ch) + 1) % 10))
        else:
            # 其他字符不变
            result.append(ch)
    return ''.join(result)

def decrypt(t: str) -> str: # 解密函数
    result = []
    for ch in t:
        if 'a' <= ch <= 'z':
            # 小写字母原为大写字母 + 后移一位
            if ch == 'a':
                result.append('Z')
            else:
                result.append(chr(ord(ch.upper()) - 1))
        elif 'A' <= ch <= 'Z':
            # 大写字母原为小写字母 + 后移一位
            if ch == 'A':
                result.append('z')
            else:
                result.append(chr(ord(ch.lower()) - 1))
        elif '0' <= ch <= '9':
            # 数字-1，0→9
            result.append(str((int(ch) - 1) % 10))
        else:
            # 其他字符不变
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    s = input()
    t = input()
    print(encrypt(s))
    print(decrypt(t))