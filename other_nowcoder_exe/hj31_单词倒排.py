import re

def reverse_words(sentence):
    # 使用正则表达式提取所有由字母组成的单词
    words = re.findall(r'[a-zA-Z]+', sentence)
    # 将单词列表逆序
    reversed_words = words[::-1]
    # 用空格连接并返回
    return ' '.join(reversed_words)

# 读取输入
input_sentence = input().strip()

# 处理并输出结果
print(reverse_words(input_sentence))