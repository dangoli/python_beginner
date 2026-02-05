from typing import List
from math import inf

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -inf
        i = 0
        while i < n:
            # 第一段
            start = i
            i += 1
            while i < n and nums[i - 1] < nums[i]:
                i += 1
            if i == start + 1:  # 第一段至少要有两个数
                continue

            # 第二段
            peak = i - 1
            res = nums[peak - 1] + nums[peak]  # 第一段的最后两个数必选
            while i < n and nums[i - 1] > nums[i]:
                res += nums[i]  # 第二段的所有元素必选
                i += 1
            if i == peak + 1 or i == n or nums[i - 1] == nums[i]:  # 第二段至少要有两个数，第三段至少要有两个数
                continue

            # 第三段
            bottom = i - 1
            res += nums[i]  # 第三段的前两个数必选（第一个数在上面的循环中加了）
            # 从第三段的第三个数往右，计算最大元素和
            max_s = s = 0
            i += 1
            while i < n and nums[i - 1] < nums[i]:
                s += nums[i]
                max_s = max(max_s, s)
                i += 1
            res += max_s

            # 从第一段的倒数第三个数往左，计算最大元素和
            max_s = s = 0
            for j in range(peak - 2, start - 1, -1):
                s += nums[j]
                max_s = max(max_s, s)
            res += max_s
            ans = max(ans, res)

            i = bottom  # 第三段的起点也是下一个极大三段式子数组的第一段的起点
        return ans