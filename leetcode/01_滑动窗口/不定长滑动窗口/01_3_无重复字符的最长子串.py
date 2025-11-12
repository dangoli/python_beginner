class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        l = 0
        letter_set = {}
        for r, ch in enumerate(s):
            # 右移右指针，出现重复的左移左指针直到无重复
            if ch in letter_set and letter_set[ch] >= l:
                l = letter_set[ch] + 1
            letter_set[ch] = r
            max_l = max(max_l, r - l + 1)
        return max_l
    
s = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(s)) 