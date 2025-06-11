def identical(pw: str) -> bool: # 定义重复子串验证函数
    n = len(pw)
    max_l = n // 2 # 最长子串长度
    for l in range(3, max_l + 1):
        first_occur = {} # 字典记录子串第一次出现的位置
        for i in range(0, n - l + 1):
            sub = pw[i:i + l] # 当前子串
            if sub not in first_occur: # 如果子串第一次出现
                first_occur[sub] = i # 记录子串首次出现位置1
            else:
                j = first_occur[sub] # 如果子串已经出现过
                if j + l <= i: # 如果子串不重叠
                    return False # 存在不重叠的重复子串
    return True # 没有不重叠的重复子串

pw = "asdwdf123%$^7dgASDFtwrsv%^asdw" # 测试用例
identical_result = identical(pw)
print(f"Identical result: {identical_result}")