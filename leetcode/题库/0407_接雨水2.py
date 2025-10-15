import heapq

class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = [] # 最小堆
        # 初始化，将四周边界加入堆
        for i in range(m):
            for j in [0, n - 1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in range(n):
                if not visited[i][j]:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        # BFS方向
        dirs = [(1, 0),(-1, 0),(0, 1),(0,-1)]
        res = 0

        # 不断弹出最低的墙
        while heap:
            height, x, y = heapq.heappop(heap)
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # 如果邻居比当前墙低，则能积水
                    if heightMap[nx][ny] < height:
                        res += height - heightMap[nx][ny]
                    # 邻居的有效高度 = max(邻居高度，当前墙高)
                    heapq.heappush(heap, (max(height, heightMap[nx][ny], nx, ny)))
        return res
    
heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
s = Solution()
print(s.trapRainWater(heightMap))