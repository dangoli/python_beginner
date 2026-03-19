class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        max_wt = -1
        for x, y, wt in edges:
            if online[x] and online[y]:
                g[x].append((y, wt))
                if x == 0:
                    max_wt = max(max_wt, wt)

        def check(lower: int) -> bool:
            @cache
            def dfs(x: int) -> int:
                if x == n - 1:  # 到达终点
                    return 0
                res = inf
                for y, wt in g[x]:
                    if wt >= lower:
                        res = min(res, dfs(y) + wt)
                return res
            return dfs(0) <= k

        left, right = -1, max_wt + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left