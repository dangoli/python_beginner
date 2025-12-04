from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.pos = defaultdict(list)
        for i, v in enumerate(arr):
            self.pos[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.pos:
            return 0
        arr = self.pos[value]

        l = bisect_left(arr, left)
        r = bisect_right(arr, right)
        return r - l
    
cmds = ["RangeFreqQuery", "query", "query"]
args = [
    [[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], 
    [1, 2, 4], 
    [0, 11, 33]
]
res = []
obj = None
for cmd, arg in zip(cmds, args):
    if cmd == "RangeFreqQuery":
        obj = RangeFreqQuery(*arg)
        res.append(None)
    else:
        out = getattr(obj, cmd)(*arg)
        res.append(out)

print(res)