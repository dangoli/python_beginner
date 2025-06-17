def sort_string(s):
    # 提取字母，保持顺序，排序时忽略大小写
    letters = [c for c in s if c.isalpha()]
    sorted_letters = sorted(letters, key=lambda x: x.lower())

    result = []
    letter_index = 0

    # 遍历原始字符串，构建最终结果
    for c in s:
        if c.isalpha():
            result.append(sorted_letters[letter_index])
            letter_index += 1
        else:
            result.append(c)
    return ''.join(result)

if __name__ == '__main__':
    try:
        str = input()
        output = sort_string(str)
        print(output)
    except EOFError:
        pass