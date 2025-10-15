from typing import List
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        max_damage = 0
        for i in range(0, len(power)): # 两层嵌套
            power_new = power.pop(i) # 剩余可以选用的咒语
            list_forbidden = [] # 不能使用的伤害
            damage = 0 # 记录当前选用的咒语施加的伤害
            a, b, c, d = i-2, i-1, i+1, i+2
            list_forbidden.extend([a, b, c, d])
            if power[i] not in list_forbidden:
                damage += power[i]
        return max_damage
    
power = [7,1,6,6]
s = Solution()
print(s.maximumTotalDamage(power))