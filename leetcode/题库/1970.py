from typing import List

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        DIRS = (0, -1), (0, 1), (-1, 0), (1, 0)  # 左右上下

        # 0：水
        # 1：陆地（未被感染）
        # 2：陆地（已被感染）
        state = [[0] * col for _ in range(row)]

        # 能否从第一行到达 (r, c)
        def can_reach_from_top(r: int, c: int) -> bool:
            if r == 0:  # 已经是第一行
                return True
            for dx, dy in DIRS:
                x, y = r + dx, c + dy
                if 0 <= x < row and 0 <= y < col and state[x][y] == 2:
                    return True
            return False

        # 从 (r, c) 出发，能否到达最后一行
        def dfs(r: int, c: int) -> bool:
            if r == row - 1:
                return True
            state[r][c] = 2  # 感染
            for dx, dy in DIRS:
                x, y = r + dx, c + dy
                # 传播病毒到未被感染的陆地
                if 0 <= x < row and 0 <= y < col and state[x][y] == 1 and dfs(x, y):
                    return True
            return False

        for day in range(len(cells) - 1, -1, -1):
            r, c = cells[day]
            r -= 1  # 改成从 0 开始的下标
            c -= 1
            state[r][c] = 1  # 未被感染的陆地
            if can_reach_from_top(r, c) and dfs(r, c):
                return day