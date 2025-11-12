from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_n = 0
        l = 0
        count = {}
        for r, fruit in enumerate(fruits):
            count[fruit] = count.get(fruit, 0) + 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            max_n = max(max_n, r - l + 1)
        return 0