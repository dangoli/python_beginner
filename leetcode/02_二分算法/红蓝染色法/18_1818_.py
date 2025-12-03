from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        location = 0
        difference = 0
        s = 0
        for i in range(len(nums1)):
            d = nums1[i] - nums2[i]
            difference_now = d if d >= 0 else d * (-1) # 目前的差
            s += difference_now
            if difference_now > difference:
                location = i
            difference = max(difference_now, difference)
        s = s - difference # 先减掉最大差
        n = nums2[location]
        nums1.sort()
        d_l = nums1[bisect_left(nums1, n) - 1] - n
        d_l = d_l if d_l >= 0 else d_l*(-1)
        d_r = nums1[bisect_right(nums1, n)] - n
        d_r = d_r if d_r >= 0 else d_r*(-1)
        if d_l < d_r:
            s += d_l
        else:
            s += d_r
        return s
    
nums1 = [1,10,4,4,2,7] 
nums2 = [9,3,5,1,7,4]
s = Solution()
print(s.minAbsoluteSumDiff(nums1, nums2))