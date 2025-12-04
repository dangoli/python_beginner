import bisect
from collections import defaultdict
from typing import List

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        """
        使用 persons 和 times 数组初始化对象。
        此方法将预处理在每个时间点的领先候选人，以便后续快速查询。
        """
        self.times = times
        # leaders[i] 将存储在时间 times[i] 时的领先候选人
        self.leaders = []
        
        # 使用字典来跟踪每个候选人的票数
        vote_counts = defaultdict(int)
        
        # 当前领先的候选人
        current_leader = -1
        # 当前领先者拥有的最大票数
        max_votes = 0
        
        # 遍历所有投票，模拟选举过程
        for person in persons:
            # 为当前候选人增加一票
            vote_counts[person] += 1
            
            # 检查是否需要更新领先者
            # 规则：如果当前候选人的票数大于或等于已知最高票数，
            # 则该候选人成为新的领先者。
            # '='号处理了平局情况，即最近获得投票的候选人获胜。
            if vote_counts[person] >= max_votes:
                max_votes = vote_counts[person]
                current_leader = person
            
            # 记录在当前时间点的领先者
            self.leaders.append(current_leader)

    def q(self, t: int) -> int:
        """
        根据前面描述的规则，返回在时刻 t 在选举中领先的候选人的编号。
        我们需要在 times 数组中找到小于等于 t 的最大时间点。
        """
        # bisect_right 返回一个插入点，该点在数组中所有值为 t 的元素之后。
        # 例如，对于 times = [5, 10, 15] 和 t = 12, bisect_right 返回 2。
        # 这意味着 times[0] 和 times[1] 是 <= 12 的。
        # 我们需要的是最后一个 <= t 的元素的索引，所以是 i - 1。
        # 对于 t = 12，i = 2，目标索引是 2 - 1 = 1。
        # 我们关心的领先者是 leaders[1]。
        i = bisect.bisect_right(self.times, t) - 1
        
        # 根据题目保证, t >= times[0], 所以 i 不会是负数。
        # 返回在对应时间点的领先候选人
        return self.leaders[i]

cmds = ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
args = [
    [[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], 
    [3], 
    [12], 
    [25], 
    [15], 
    [24], 
    [8]
]

obj = None
res = []

for c, a in zip(cmds, args):
    if c == "TopVotedCandidate":
        persons, times = a
        obj = TopVotedCandidate(persons, times)
        res.append(None)
    else:  # 调用 q()
        t = a[0]
        res.append(obj.q(t))

print(res)