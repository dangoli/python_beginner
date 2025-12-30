from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m - 2):
            for j in range(n - 2):
                if grid[i + 1][j + 1] != 5:
                    continue

                mask = 0
                r_sum = [0] * 3
                c_sum = [0] * 3
                for r in range(3):
                    for c in range(3):
                        x = grid[i + r][j + c]
                        mask |= 1 << x
                        r_sum[r] += x
                        c_sum[c] += x

                if mask == 1022 and r_sum[0] == r_sum[1] == c_sum[0] == c_sum[1] == 15:
                    ans += 1

        return ans