def longest_palindrome_length(s: str) -> int: #  计算最长回文子串的长度
    max_len = 0
    n = len(s)
    
    for i in range(n):
        # 奇数长度回文
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            max_len = max(max_len, r - l + 1)
            l -= 1
            r += 1
        
        # 偶数长度回文
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            max_len = max(max_len, r - l + 1)
            l -= 1
            r += 1
    
    return max_len

# 主程序
s = input().strip()
print(longest_palindrome_length(s))