from typing import List
from functools import cache
from math import inf

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # 返回从 nums1[:i+1] 和 nums2[:j+1] 中选两个长度相同的【非空】子序列的最大点积
        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                # 其中一个数组没有元素，无法选出非空子序列
                return -inf  # 下面计算 max 不会取到无解情况

            # 选 nums1[i] 和 nums2[j]
            # 和前面的子序列拼起来，或者不拼（作为子序列的第一个数）
            res1 = max(dfs(i - 1, j - 1), 0) + nums1[i] * nums2[j]

            # 不选 nums1[i]
            res2 = dfs(i - 1, j)

            # 不选 nums2[j]
            res3 = dfs(i, j - 1)

            return max(res1, res2, res3)

        return dfs(len(nums1) - 1, len(nums2) - 1)