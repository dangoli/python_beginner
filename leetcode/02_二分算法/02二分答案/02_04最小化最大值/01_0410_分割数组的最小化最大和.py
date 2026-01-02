from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mx: int) -> bool:
            cnt = 1
            s = 0
            for x in nums:
                if s + x <= mx:
                    s += x
                    continue
                if cnt == k:  # 不能继续划分
                    return False
                cnt += 1  # 新划分一段
                s = x
            return True

        left = max(nums) - 1
        right = sum(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right
    
nums = [7,2,5,10,8]
k = 2
s = Solution()
print(s.splitArray(nums,k))