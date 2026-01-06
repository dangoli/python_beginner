from typing import List
from math import inf

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = neg_cnt = 0
        mn = inf
        for row in matrix:
            for x in row:
                if x < 0:
                    neg_cnt += 1
                    x = -x  # 先把负数都变成正数
                mn = min(mn, x)
                total += x

        if neg_cnt % 2:
            total -= mn * 2  # 给绝对值最小的数添加负号
        return total