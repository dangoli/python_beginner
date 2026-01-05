from typing import List
# 二分查找

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # 方向数组，上、下、左、右
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(heights)
        n = len(heights[0])

        # 检查在最大允许消耗为 effort 的条件下
        # 是否存在一条从 (x, y) 到达终点 (m-1, n-1) 的有效路径
        def dfs(x, y, effort, visited):
            # 已经到达终点
            if x == m - 1 and y == n - 1:
                return True
            
            # 标记当前单元格为已访问，防止在路径中重复访问（成环）
            visited[x][y] = True
            
            # 遍历四个相邻方向
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                
                # 检查下一个位置是否越界或已被访问
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # 计算移动到下一个单元格的体力消耗
                    cost = abs(heights[nx][ny] - heights[x][y])
                    
                    # 如果消耗在允许的 effort 范围内
                    if cost <= effort:
                        # 从相邻格子出发能到达终点，则说明当前路径可行
                        if dfs(nx, ny, effort, visited):
                            return True
            
            # 无法到达终点
            return False
        
        
        # 左边界为0，右边界为10^6，可以换成网格中最大值
        l, r = 0, 1000000
        
        while l < r:
            # 当前猜测的 "最大允许体力消耗"
            mid = l + (r - l) // 2
            
            # 检查在此消耗下，能否从起点到达终点
            # 每次检查都需要一个全新的 visited 数组
            visited = [[False] * n for _ in range(m)]
            if dfs(0, 0, mid, visited):
                # mid 是一个可行解，意味着可能还有更小的解，所以缩小右边界
                r = mid
            else:
                # mid 不可行，说明需要更大的消耗，所以增大左边界
                l = mid + 1
        
        return l