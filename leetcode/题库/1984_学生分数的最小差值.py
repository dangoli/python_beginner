from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        diff = []
        for i in range(1, len(nums)):
            diff.append(nums[i] - nums[i-1])
        
        vowel = 0
        for i,c in enumerate(diff):
            #1.右端点进入窗口
            vowel += c

            left = i - k + 2 # 左端点
            if left < 0 :
                continue

            # 比较右边待进入，小则加，
            if diff[i + 1] < diff[left]:
                vowel = vowel - diff[left] + diff[i + 1]
        return vowel
    
nums = [9,4,1,7]
k = 2
s = Solution()
print(s.minimumDifference(nums, k))