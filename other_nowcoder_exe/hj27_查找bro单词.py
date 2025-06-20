def is_brother(word, target):
    return word != target and sorted(word) == sorted(target)

if __name__ == "__main__":
    # 输入并解析
    str = input().split()
    n = int(str[0])
    lst = str[1:n+1]
    x = str[n+1]
    k = int(str[n+2])
    
    # 找出兄弟单词
    brothers = [word for word in lst if is_brother(word, x)]
    
    # 兄弟单词数量
    print(len(brothers))
    
    # 按字典序排序
    brothers.sort()
    
    # 输出第 k 个兄弟单词（1-based index）
    if k <= len(brothers):
        print(brothers[k-1])