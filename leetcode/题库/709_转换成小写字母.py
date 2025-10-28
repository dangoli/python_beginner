class Solution:
    def toLowerCase(self, s: str) -> str:
        # 用ASCII码转换
        res = []    
        for c in s:
            if ord('A') <= ord(c) <= ord('Z'):
                res.append(chr(ord(c) + 32))
            else:
                res.append(c)
        return ''.join(res)