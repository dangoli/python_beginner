class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        groups = defaultdict(list)  # 三角形底部两个字母 -> [三角形顶部字母]
        for s in allowed:
            groups[s[:2]].append(s[2])

        n = len(bottom)
        pyramid = [[''] * (i + 1) for i in range(n)]
        pyramid[-1] = bottom

        # 现在准备填 (i, j) 这个格子
        # 返回继续填能否填完所有格子（从下往上填，每行从左到右填）
        def dfs(i: int, j: int) -> bool:
            if i < 0:  # 所有格子都已填完
                return True

            if j == i + 1:  # i 行已填完
                return dfs(i - 1, 0)  # 开始填 i-1 行

            # 枚举 (i, j) 填什么字母
            # 这取决于 (i+1, j) 和 (i+1, j+1) 填的字母
            for top in groups[pyramid[i + 1][j] + pyramid[i + 1][j + 1]]:
                pyramid[i][j] = top
                if dfs(i, j + 1):
                    return True
            return False

        # 从倒数第二行开始填
        return dfs(n - 2, 0)