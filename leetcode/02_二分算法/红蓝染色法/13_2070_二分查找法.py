from typing import List
from bisect import bisect_right

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda i:i[0]) # 按照价格大小升序排序
        for i in range(1, len(items)):
            # 原地计算beauty的前缀最大值
            items[i][1] = max(items[i][1], items[i-1][1])

        for i, q in enumerate(queries):
            j = bisect_right(items, q, key=lambda i:i[0])
            queries[i] = items[j - 1][1] if j else 0
        return queries