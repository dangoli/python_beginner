"""
在本题中，我们需要处理文件报错信息，其由出错文件的文件路径和错误行号组成。文件路径的前三个字母为大写字母A-Z 冒号":" 和反斜杠"\", 代表盘符。
随后是若干由小写字母构成的字符串，代表文件夹名，彼此使用单个反斜杠间隔。路径的最后一个反斜杠后是文件名。
我们只在乎文件名（即去掉除了文件名以外的全部信息），且至多保留文件名的最后16个字符。
随后，我们需要统计相同的报错信息：如果两条报错信息保留后16个字符后的文件名相同，且行号相同，则视为同一个报错.
相同的报错信息以第一次出现的时间为准，至多输出最后8条记录。
输入描述:
本题将会给出1≦T≦100条报错信息，确切数字未知，您需要一直读入直到文件结尾。
在一行上先输入一个长度为1≦length(x)≦100 的字符串x代表文件路径；随后，在同一行输入一个整数y(1≦y≦1000) 代表行号。文件路径的格式如题干所述，保证文件名不为空。
输出描述:
至多八行，每行先输出一个长度为1≦length(s)≦16 的字符串s，代表文件名；随后，在同一行输出错误行号、报错次数。
"""
"""
字符串处理, 去重统计, 保留顺序
"""

import sys

def main():
    records = []          # 保存报错的顺序
    count_map = {}        # key: (filename, line)  value: count

    for line in sys.stdin:
        line = line.strip()
        if not line: # 用户只回车
            break
        try:
            path, lineno = line.rsplit(" ", 1) # 从右边分割, 只分割一次
        except ValueError:
            continue
        lineno = int(lineno)

        # 取出文件名
        filename = path.split("\\")[-1] # 最后一个文件名 转义字符

        # 保留最后16个字符
        if len(filename) > 16:
            filename = filename[-16:]

        key = (filename, lineno) # 作为字典的key
        if key not in count_map: # 第一次出现
            count_map[key] = 1
            records.append(key)  # 记录出现顺序
        else:
            count_map[key] += 1

    # 只输出最后8条
    for key in records[-8:]:
        filename, lineno = key
        print(filename, lineno, count_map[key])


if __name__ == "__main__":
    main()