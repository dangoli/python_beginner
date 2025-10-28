class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        arr = [1 if c == 'W' else 0 for c in blocks]
        s = sum(arr[:k])
        ans = s
        for i in range(k, len(arr)):
            s += arr[i] - arr[i - k]
            ans = min(ans, s)
        return ans
    
blocks = "WBWBBBW"
k = 2
s = Solution()
print(s.minimumRecolors(blocks, k))