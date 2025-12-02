from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.dct = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dct[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        return "" if (a:=bisect_right(self.dct[key], [timestamp, "z" * 101])) == 0 else self.dct[key][a-1][1]