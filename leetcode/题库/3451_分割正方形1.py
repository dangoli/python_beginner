from typing import List
from collections import defaultdict
from itertools import pairwise

"""
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        M = 100_000
        total_area = sum(l * l for _, _, l in squares)

        def check(y: float) -> bool:
            area = 0
            for _, yi, l in squares:
                if yi < y:
                    area += l * min(y - yi, l)
            return area >= total_area / 2

        left = 0
        right = max_y = max(y + l for _, y, l in squares)
        for _ in range((max_y * M).bit_length()):
            mid = (left + right) / 2
            if check(mid):
                right = mid
            else:
                left = mid
        return (left + right) / 2  # 区间中点误差小
"""

"""
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        M = 100_000
        total_area = sum(l * l for _, _, l in squares)

        def check(multi_y: int) -> bool:
            area = 0
            for _, y, l in squares:
                if y * M < multi_y:
                    area += l * min(multi_y - y * M, l * M)
            return area * 2 >= total_area * M

        max_y = max(y + l for _, y, l in squares)
        return bisect_left(range(max_y * M), True, key=check) / M
"""

"""
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def calc_area(y: int) -> int:
            area = 0
            for _, yi, l in squares:
                if yi < y:
                    area += l * min(y - yi, l)
            return area

        tot_area = sum(l * l for _, _, l in squares)
        max_y = max(y + l for _, y, l in squares)
        y = bisect_left(range(max_y), tot_area, key=lambda y: calc_area(y) * 2)

        area_y = calc_area(y)
        sum_l = area_y - calc_area(y - 1)
        return y - (area_y * 2 - tot_area) / (sum_l * 2)  # 这样写误差更小
"""

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        tot_area = 0
        diff = defaultdict(int)
        for _, y, l in squares:
            tot_area += l * l
            diff[y] += l
            diff[y + l] -= l

        area = sum_l = 0
        for y, y2 in pairwise(sorted(diff)):
            sum_l += diff[y]  # 矩形底边长度之和
            area += sum_l * (y2 - y)  # 底边长 * 高 = 新增面积
            if area * 2 >= tot_area:
                return y2 - (area * 2 - tot_area) / (sum_l * 2)