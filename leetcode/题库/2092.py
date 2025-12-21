from collections import defaultdict
from typing import List

class Solution:
    def findAllPeople(self, _, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # 按照 time 从小到大排序
        meetings.sort(key=lambda m: m[2])

        # 一开始 0 和 firstPerson 都知道秘密
        have_secret = {0, firstPerson}

        # 分组循环
        m = len(meetings)
        i = 0
        while i < m:
            # 在同一时间发生的会议，建图
            g = defaultdict(list)
            time = meetings[i][2]
            while i < m and meetings[i][2] == time:
                x, y, _ = meetings[i]
                g[x].append(y)
                g[y].append(x)
                i += 1

            # 每个连通块只要有一个人知道秘密，那么整个连通块的人都知道秘密
            vis = set()  # 避免重复访问节点

            def dfs(x: int) -> None:
                vis.add(x)
                have_secret.add(x)
                for y in g[x]:
                    if y not in vis:
                        dfs(y)

            # 遍历在 time 时间点参加会议的专家
            for x in g:
                # 从知道秘密的专家出发，DFS 标记其余专家
                if x in have_secret and x not in vis:
                    dfs(x)

        # 可以按任何顺序返回答案
        return list(have_secret)