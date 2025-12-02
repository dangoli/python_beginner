from collections import deque, defaultdict
from typing import List
from bisect import bisect_left, bisect_right


class Router:
    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.packet_q = deque() # 队列
        self.packet_set = set() # 集合来管理数据包
        self.destination_to_timestamps = defaultdict(deque) # 

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False
        self.packet_set.add(packet)
        if len(self.packet_q) == self.memory_limit:
            self.forwardPacket() # 太多了就先进先出
        self.packet_q.append(packet) # 入队
        self.destination_to_timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packet_q: # 如果是空的
            return []
        packet = self.packet_q.popleft() # 让最先进去的出队
        self.packet_set.remove(packet)
        self.destination_to_timestamps[packet[1]].popleft()
        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = list(self.destination_to_timestamps[destination])
        left = bisect_left(timestamps, startTime)  # deque 访问不是 O(1) 的，可以看另一份代码【Python3 list】
        right = bisect_right(timestamps, endTime)
        return right - left
    
commands = ["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]
params = [[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]

result = []
router = None
for cmd, param in zip(commands, params):
    if cmd == "Router":
        router = Router(param[0])
        result.append(None)
    elif cmd == "addPacket":
        result.append(router.addPacket(*param))
    elif cmd == "forwardPacket":
        result.append(router.forwardPacket())
    elif cmd == "getCount":
        result.append(router.getCount(*param))

print(result)