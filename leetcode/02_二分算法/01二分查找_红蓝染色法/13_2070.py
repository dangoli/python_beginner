from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x:x[0]) # 按照[i,0]大小排序, 按照物品价格排序
        idx = sorted(range(len(queries)), key=lambda i: queries[i]) # 元素大小升序排序，返回索引
        ans = [0] * len(queries)
        max_beauty = j = 0
        for i in idx:
            q = queries[i]
            # 增量地遍历满足 queries[i-1] < price <= queries[i]的物品
            while j < len(items) and items[j][0] <= q:
                max_beauty = max(max_beauty, items[j][1])
                j += 1
            ans[i] = max_beauty
        return ans

items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [7,1,2,3,4,5,6]
s = Solution()
print(s.maximumBeauty(items, queries))