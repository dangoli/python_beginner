#枚举k

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = max_diff = pre_max = 0
        for x in nums:
            ans = max(ans, max_diff * x)
            max_diff = max(max_diff, pre_max - x)
            pre_max = max(pre_max, x)
        return ans


    
nums = [12,6,1,2,7]
s = Solution()
print(s.maximumTripletValue(nums))